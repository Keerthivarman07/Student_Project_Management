from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserType(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        FACULTY = "FACULTY", "Faculty"
        HOD = "HOD", "Head of Department"

    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.STUDENT,
    )

    # later we can add more fields like phone, etc.

    def __str__(self):
        return f"{self.username} ({self.user_type})"

from django.conf import settings


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)          # e.g. "CSE", "IT"
    full_name = models.CharField(max_length=200)                  # e.g. "Computer Science and Engineering"

    def __str__(self):
        return self.name


class Batch(models.Model):
    """
    One final-year batch, e.g. 2025-2026.
    """
    name = models.CharField(max_length=20, unique=True)           # "2025-2026"
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.name


class ClassSection(models.Model):
    """
    A class inside a department, like CSE-A, CSE-B.
    """
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)                        # "CSE-A"

    class Meta:
        unique_together = ("department", "batch", "name")

    def __str__(self):
        return f"{self.name} ({self.batch})"


class FacultyProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=50, unique=True)
    is_hod = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.employee_id}"


class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=50, unique=True)
    semester = models.IntegerField()

    def __str__(self):
        return f"{self.roll_number} - {self.user.get_full_name() or self.user.username}"
