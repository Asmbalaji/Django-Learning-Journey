from django.contrib import admin
from .models import Employee


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