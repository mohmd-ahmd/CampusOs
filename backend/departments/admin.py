from django import forms
from django.contrib import admin
from django.http import JsonResponse, HttpResponseForbidden
from django.urls import path, reverse

from .models import Department, CampusDepartment


class CampusDepartmentAdminForm(forms.ModelForm):

    class Meta:
        model = CampusDepartment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # URL used by JavaScript to fetch available departments
        self.fields["campus"].widget.attrs[
            "data-available-departments-url"
        ] = reverse(
            "admin:departments_campusdepartment_available_departments"
        )

        # Identify the selected campus
        campus_id = self.data.get(
            self.add_prefix("campus")
        )

        if not campus_id and self.instance.pk:
            campus_id = self.instance.campus_id

        if not campus_id:
            initial_campus = self.initial.get("campus")
            campus_id = getattr(initial_campus, "pk", initial_campus)

        try:
            campus_id = int(campus_id) if campus_id else None
        except (TypeError, ValueError):
            campus_id = None

        # Initially, no departments are available without a campus
        if not campus_id:
            self.fields["department"].queryset = Department.objects.none()
            return

        # Find departments already assigned to this campus
        existing_assignments = CampusDepartment.objects.filter(
            campus_id=campus_id
        )

        # Allow the current department when editing an existing assignment
        if self.instance.pk:
            existing_assignments = existing_assignments.exclude(
                pk=self.instance.pk
            )

        assigned_ids = existing_assignments.values_list(
            "department_id",
            flat=True
        )

        available_departments = Department.objects.all()

        if not self.instance.pk:
            available_departments = available_departments.filter(
                is_active=True
            )

        self.fields["department"].queryset = (
            available_departments.exclude(
                id__in=assigned_ids
            )
        )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "code",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "code",
    )

    list_filter = ("is_active",)


@admin.register(CampusDepartment)
class CampusDepartmentAdmin(admin.ModelAdmin):

    form = CampusDepartmentAdminForm

    list_display = (
        "campus",
        "department",
        "is_active",
        "created_at",
    )

    search_fields = (
        "campus__name",
        "department__name",
        "department__code",
    )

    list_filter = (
        "campus",
        "department",
        "is_active",
    )

    class Media:
        js = (
            "departments/js/campus_department_admin.js",
        )

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path(
                "available-departments/",
                self.admin_site.admin_view(
                    self.available_departments
                ),
                name="departments_campusdepartment_available_departments",
            ),
        ]

        return custom_urls + urls

    def available_departments(self, request):

        if not (
            self.has_add_permission(request)
            or self.has_change_permission(request)
        ):
            return HttpResponseForbidden()

        campus_id = request.GET.get("campus_id")

        try:
            campus_id = int(campus_id)
        except (TypeError, ValueError):
            return JsonResponse({"results": []})

        assigned_ids = CampusDepartment.objects.filter(
            campus_id=campus_id
        ).values_list(
            "department_id",
            flat=True
        )

        departments = Department.objects.filter(
            is_active=True
        ).exclude(
            id__in=assigned_ids
        ).order_by(
            "name",
            "code"
        )

        results = [
            {
                "id": department.id,
                "text": f"{department.name} ({department.code})"
            }
            for department in departments
        ]

        return JsonResponse({"results": results})