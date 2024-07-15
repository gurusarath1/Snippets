from django.contrib import admin
from testapp_lesson_4_database_admin.models import Student

# Register your models here.
# http://127.0.0.1:8000/admin/testapp_lesson_4_database_admin/student/
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','age','score'] # There are the list of things that we want to display in our admin page


#admin.site.register(Student)   #OR
admin.site.register(Student, StudentAdmin)



'''
HOW TO CREATE ADMIN LOGIN

(web_dev) G:\Guru_Sarath\Study\WebDevelopment\Django\learning_web_app>python manage.py createsuperuser
Username (leave blank to use 'gurus'): gurus
Email address: gurusarat1.official@gmail.com
Password:gst
Password (again):gst
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
'''