from .models import Student
from django.shortcuts import render
from .models import Student
from django.shortcuts import render


def dashboard(request):
    students = Student.objects.all()

    total_students = students.count()
    passed_students = students.filter(marks__gte=50).count()
    failed_students = students.filter(marks__lt=50).count()

    context = {
        'total_students': total_students,
        'passed_students': passed_students,
        'failed_students': failed_students,
    }

    return render(request, 'core/dashboard.html', context)
def home(request):

    students = []

    if request.method == "POST":

        for i in range(1, 5):

            name = request.POST.get(f"name{i}")
            age = request.POST.get(f"age{i}")
            marks = int(request.POST.get(f"marks{i}"))

            if marks >= 50:
                result = "Pass"
            else:
                result = "Fail"

            student = {
                "name": name,
                "age": age,
                "marks": marks,
                "result": result
            }

            students.append(student)

    return render(request, "core/home.html", {
        "students": students
    })