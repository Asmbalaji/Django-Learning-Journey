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