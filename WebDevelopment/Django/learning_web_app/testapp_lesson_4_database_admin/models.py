from django.db import models

class Student(models.Model):

    name = models.CharField(max_length=50)
    score = models.PositiveIntegerField()
    age = models.PositiveBigIntegerField()
    email = models.EmailField()


    def __str__(self):
        return self.name
    
    class Meta:
        # Default ordering when viewing the database (in this care in our admin page)
        ordering = ['-age'] # - sign for descending order



'''
SHELL COMMANDS

python manage.py shell

>>> from testapp_lesson_4_database_admin.models import Student


'''