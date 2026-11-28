from django.db import models
from organizations.models import Campus

class Department(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Department Name'
    )

    code = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Department Code'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Description'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Active Status'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    class Meta:
        ordering = ['name']
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
    def __str__(self):
        return f"{self.name} ({self.code})"

class CampusDepartment(models.Model):

        campus = models.ForeignKey(
            Campus,
            on_delete=models.PROTECT,
            related_name='campus_departments'
        )

        department = models.ForeignKey(
            Department,
            on_delete=models.PROTECT,
            related_name='campus_assignments'
        )

        is_active = models.BooleanField(
            default=True,
            verbose_name='Active Status'
        )
        created_at = models.DateTimeField(
            auto_now_add=True
        )

        class Meta:
            ordering = ["campus__name", "department__name"]

            verbose_name = "Campus Department"
            verbose_name_plural = "Campus Departments"

            constraints = [
                models.UniqueConstraint(
                    fields=["campus", "department"],
                    name="unique_department_per_campus"
                )
            ]

        def __str__(self):
            return f"{self.department.name} - {self.campus.name}"
# Create your models here.
