from django.db import models

class Person(models.Model): 
    name = models.CharField(max_length=20) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20) 



'''
LEARNING -------------------------

python manage.py shell

>>> from testapp_lesson_2_database.models import Person
>>> Person.objects.all()
'''