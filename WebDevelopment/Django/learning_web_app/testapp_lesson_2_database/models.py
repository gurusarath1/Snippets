from django.db import models

class Person(models.Model): 
    name = models.CharField(max_length=20) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20)

    # This function enables printing the odatabase object
    def __str__(self):
        return self.name # We print only the name



'''
LEARNING -------------------------

python manage.py makemigration
python manage.py migrate


------------------------------------

python manage.py shell

>>> from testapp_lesson_2_database.models import Person
>>> Person.objects.all()
>>> p = Person(name='Guru', email='gg@g.com', phone=1234)
>>> p.save()
'''