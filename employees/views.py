
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.db.models import Sum, Count
from .models import Employee, EmployeeWorkLog
from django.db.models import Sum, Count, Q
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

    return render(request, 'employees/register.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()

    return render(
        request,
        'employees/employee_list.html',
        {'employees': employees}
    )


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

def employee_performance(request):

    employees = Employee.objects.prefetch_related('work_logs')

    performance_data = []

    for employee in employees:

        logs = employee.work_logs.all()

        total_hours = logs.aggregate(
            total=Sum('hours_worked')
        )['total'] or 0

        total_tasks = logs.aggregate(
            total=Sum('tasks_assigned')
        )['total'] or 0

        completed_tasks = logs.aggregate(
            total=Sum('tasks_completed')
        )['total'] or 0

        total_days = logs.count()

        present_days = logs.filter(
            attendance='PRESENT'
        ).count()

        attendance_percentage = (
            (present_days / total_days) * 100
            if total_days else 0
        )

        performance = (
            (completed_tasks / total_tasks) * 100
            if total_tasks else 0
        )

        performance_data.append({
            'employee': employee,
            'total_hours': total_hours,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'attendance_percentage': round(attendance_percentage, 2),
            'performance': round(performance, 2),
        })

    return render(
        request,
        'employees/performance.html',
        {'performance_data': performance_data}
    )

def employee_dashboard(request):

        total_employees = Employee.objects.count()

        total_hours = EmployeeWorkLog.objects.aggregate(
            total=Sum('hours_worked')
        )['total'] or 0

        total_tasks = EmployeeWorkLog.objects.aggregate(
            total=Sum('tasks_assigned')
        )['total'] or 0

        completed_tasks = EmployeeWorkLog.objects.aggregate(
            total=Sum('tasks_completed')
        )['total'] or 0

        departments = Employee.objects.values(
            'department'
        ).annotate(total=Count('id'))

        performance = 0
        if total_tasks > 0:
            performance = round(
                (completed_tasks / total_tasks) * 100, 2
            )

        context = {
            'total_employees': total_employees,
            'total_hours': total_hours,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'performance': performance,
            'departments': departments,
        }

        return render(request, 'employees/dashboard.html', context)