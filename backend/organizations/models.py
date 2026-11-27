
from django.db import models


class Organization(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Trust Name"
    )
    code = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="Trust Code"
    )
    email = models.EmailField(
        max_length=255,
        blank=True,
        verbose_name="Trust Email"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Contact Phone Number"
    )
    address = models.TextField(
        blank=True,
        verbose_name="Trust Address"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active Status"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Trust"
        verbose_name_plural = "Trust"

    def __str__(self):
        return self.name


class Trustee(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="trustees"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Trustee Name"
    )
    designation = models.CharField(
        max_length=100,
        verbose_name="Designation"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Trustee"
        verbose_name_plural = "Trustees"

    def __str__(self):
        return f"{self.name} - {self.designation}"


class Zone(models.Model):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="zones"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Zone Name"
    )
    code = models.CharField(
        max_length=30,
        verbose_name="Zone Code"
    )
    address = models.TextField(
        blank=True,
        verbose_name="Zone Address"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Zone"
        verbose_name_plural = "Zones"
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "code"],
                name="unique_zone_code_per_organization"
            )
        ]

    def __str__(self):
        return f"{self.name} - {self.organization.name}"


class ZoneHead(models.Model):
    zone = models.ForeignKey(
        Zone,
        on_delete=models.PROTECT,
        related_name="heads"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Zone Head Name"
    )
    designation = models.CharField(
        max_length=100,
        verbose_name="Designation"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Zone Head"
        verbose_name_plural = "Zone Heads"

    def __str__(self):
        return f"{self.name} - {self.designation}"


class Campus(models.Model):
    zone = models.ForeignKey(
        Zone,
        on_delete=models.PROTECT,
        related_name="campuses"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Campus Name"
    )
    code = models.CharField(
        max_length=30,
        verbose_name="Campus Code"
    )
    address = models.TextField(
        blank=True,
        verbose_name="Campus Address"
    )
    contact_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Contact Number"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Campus"
        verbose_name_plural = "Campuses"
        constraints = [
            models.UniqueConstraint(
                fields=["zone", "code"],
                name="unique_campus_code_per_zone"
            )
        ]

    def __str__(self):
        return f"{self.name} - {self.zone.name}"