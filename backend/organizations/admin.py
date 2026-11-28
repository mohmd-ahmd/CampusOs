from django.contrib import admin 
from departments.models import CampusDepartment
from django.forms.models import BaseInlineFormSet
from .models import (
    Organization, 
    Trustee, 
    Zone,
    ZoneHead,
    Campus
)

class TrusteeInline(admin.TabularInline):
    model = Trustee
    extra = 1

class ZoneInline(admin.TabularInline):
    model = Zone
    extra = 1

class zoneHeadInline(admin.TabularInline):
    model = ZoneHead
    extra = 1

class CampusInLine(admin.TabularInline):
    model = Campus
    extra = 1
class CampusDepartmentInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)

        existing_assignment = CampusDepartment.objects.filter(
            campus=self.instance
        )
        if form.instance.pk:
            existing_assignment = existing_assignment.exclude(
                pk=form.instance.pk
            )
        assigned_department_ids = existing_assignment.values_list(
            "department_id",
            flat=True
        )
        form.fields["department"].queryset = (
            form.fields["department"].queryset.exclude(
                id__in=assigned_department_ids
            )
        )
class CampusDepartmentInline(admin.TabularInline):
    model = CampusDepartment
    formset = CampusDepartmentInlineFormSet
    extra = 1
    

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "email",
        "phone",
        "is_active",
    )
    search_fields = ("name", "code", "email", "phone")
    list_filter = ("is_active",)
    inlines =[TrusteeInline, ZoneInline]

@admin.register(Trustee)
class TrusteeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "designation",
        "organization")
    search_fields = ("name", "designation")


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "organization",
        "is_active"
    )
    search_fields = ("name", "code",)
    list_filter = ("is_active",)
    inlines = [zoneHeadInline, CampusInLine]

@admin.register(ZoneHead)
class ZoneHeadAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "designation",
        "zone"
    )
    search_fields = ("name", "designation",)

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "zone",
        "is_active"
    )
    search_fields = ("name", "code",)
    list_filter = ("is_active",)
    inlines = [CampusDepartmentInline]
