from django.db import models


class Employee(models.Model):

    DEPARTMENTS = [
        ('IT', 'Information Technology'),
        ('HR', 'Human Resources'),
        ('FINANCE', 'Finance'),
        ('MARKETING', 'Marketing'),
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=10, unique=True)

    age = models.PositiveIntegerField()

    department = models.CharField(
        max_length=20,
        choices=DEPARTMENTS
    )

    designation = models.CharField(max_length=100)

    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    joining_date = models.DateField()

    def __str__(self):
        return self.name


from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class EmployeeWorkLog(models.Model):

    ATTENDANCE_CHOICES = [
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('LEAVE', 'Leave'),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='work_logs'
    )

    date = models.DateField(default=timezone.localdate)

    hours_worked = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(24)
        ]
    )

    attendance = models.CharField(
        max_length=10,
        choices=ATTENDANCE_CHOICES,
        default='PRESENT'
    )

    tasks_assigned = models.PositiveIntegerField(default=0)

    tasks_completed = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('employee', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

    @property
    def performance_percentage(self):
        if self.tasks_assigned == 0:
            return 0

        return round(
            (self.tasks_completed / self.tasks_assigned) * 100,
            2
        )
