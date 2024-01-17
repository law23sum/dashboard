from django.conf import settings
from django.db import models

from apps.utils.models import BaseModel


class Permit(BaseModel):
    DEPARTMENT_CHOICES = (
        ("hr", "Human Resources"),
        ("finance", "Finance"),
        ("engineering", "Engineering"),
        ("marketing", "Marketing"),
        ("sales", "Sales"),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="employees")
    department = models.CharField(
            max_length=20, choices=DEPARTMENT_CHOICES,
            help_text="What department your employee belongs to."
    )

    name = models.CharField(max_length=100, help_text="")
    name = models.CharField(max_length=100, help_text="")
    name = models.CharField(max_length=100, help_text="")

    salary = models.PositiveIntegerField(help_text="")
    salary = models.PositiveIntegerField(help_text="")
    salary = models.PositiveIntegerField(help_text="")

    def __str__(self):
        return self.name