from django.shortcuts import render

from testapp_lesson_4_database_admin.models import Student
from .forms import StudentForm



#http://127.0.0.1:8000/testapp_lesson_5/show_students/
def show_students_page(request):

    context = {}

    # Pass the Model
    students = Student.objects.all()
    context['student_db'] = students

    # Pass the form
    student_form = StudentForm()
    context['student_form'] = student_form

    return render(request, 'form_page1.html', context) 


# http://127.0.0.1:8000/testapp_lesson_5/crud_students/
def crud_students_page(request):

    context = {}

    # Pass the Model
    students = Student.objects.all()
    context['student_db'] = students

    # Pass the form
    empty_student_form = StudentForm()
    context['student_form'] = empty_student_form

    if request.method == "POST":
        if 'create'  in request.POST:
            form = StudentForm(request.POST)
            form.save()
        elif 'delete' in request.POST:
            button_value = request.POST['delete'] # Primary key of the object is stored in the button value
            student = Student.objects.get(id = button_value)
            student.delete()
        elif 'update' in request.POST:
            button_value = request.POST['update'] # Primary key of the object is stored in the button value
            student = Student.objects.get(id = button_value)
            form = StudentForm(instance=student)
            context['student_form'] = form
        elif 'save' in request.POST:
            button_value = request.POST['save']

            if not button_value:
                form = StudentForm(request.POST)
                form.save()
            else:
                student = Student.objects.get(id = button_value)
                form = StudentForm(request.POST, instance=student)
            
                form.save()




    return render(request, 'crud_form_page1.html', context)