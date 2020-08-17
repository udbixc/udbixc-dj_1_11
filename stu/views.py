from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect

# Create your views here.
from stu import models
from stu.models import Student


def add(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        age = request.POST.get('user_age')

        students = Student()
        students.name = name
        students.age = age
        students.save()

        return redirect(get)

    return render(request, 'add.html')


def get(request):
    students = Student.objects.all()
    return render(request, 'get.html', {'students':students})


def delete(request, student_id):
    Student.objects.filter(id=student_id).delete()
    return redirect(get)


def up(request, student_id):
    if request.method == 'POST':
        name = request.POST.get('up_name')
        age = request.POST.get('up_age')
        models.Student.objects.filter(id=student_id).update(name=name,age=age)
        return redirect(get)

    return render(request, 'up.html')