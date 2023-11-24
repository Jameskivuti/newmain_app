from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from main_app.app_forms import StudentForm
from main_app.models import Student


# Create your views here.
def students(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            form = StudentForm()

    form = StudentForm()
    return render(request, "students.html", {"form": form})


def show_students(request):
    # SELECT *FROM students
    # wanafunzi = Student.objects.all().order_by("-kcpe_score")
    # wanafunzi = Student.objects.filter(first_name="mercy")
    # wanafunzi = Student.objects.filter(first_name__startswith="me")
    # wanafunzi = Student.objects.filter(first_name__icontains="to", last_name__icontains="c", kcpe_score__gt=250)  # AND
    # wanafunzi = Student.objects.filter(first_name__icontains="me") | Student.objects.filter(last_name__icontains="la") #OR
    # wanafunzi = Student.objects.filter(dob__year=1997, dob__month=1)
    today = datetime.today()
    mon = today.month
    day = today.day

    wanafunzi= Student.objects.filter(dob__month=mon, dob__day=day).order_by("-first_name")
    return render(request, "display.html", {"students": wanafunzi})


def details(request, student_id):
    # SELECT * FROM students where id=1
    student = Student.objects.get(pk=student_id)
    return render(request, "details.html", {"student": student})


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect("show")
