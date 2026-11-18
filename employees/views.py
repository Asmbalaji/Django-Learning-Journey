
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


def register_employee(request):

    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm()

    return render(
        request,
        'employees/register.html',
        {'form': form}
    )


def employee_list(request):

    employees = Employee.objects.all()

    return render(
        request,
        'employees/employee_list.html',
        {'employees': employees}
    )


from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST


def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        'employees/edit_employee.html',
        {'form': form, 'employee': employee}
    )


@require_POST
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()

    return redirect('employee_list')

def edit_employee(request, pk):

    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_list')

    else:
        form = EmployeeForm(instance=employee)

    return render(
        request,
        'employees/register.html',
        {'form': form, 'employee': employee}
    )
