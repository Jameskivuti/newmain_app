from django.shortcuts import render, redirect
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
    wanafunzi = Student.objects.all()
    return render(request, "display.html", {"students": wanafunzi})


def details(request, id):
    # SELECT * FROM students where id=1
    student = Student.objects.get(pk=id)
    return render(request, "details.html", {"student": student})
