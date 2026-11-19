
from django.contrib import admin
from .models import Employee, EmployeeWorkLog


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'department',
        'designation',
        'salary'
    )

    search_fields = ('name', 'email')
    list_filter = ('department',)


@admin.register(EmployeeWorkLog)
class EmployeeWorkLogAdmin(admin.ModelAdmin):
    list_display = (
        'employee',
        'date',
        'hours_worked',
        'attendance',
        'tasks_assigned',
        'tasks_completed',
    )

    list_filter = ('attendance', 'date')
    search_fields = ('employee__name',)
