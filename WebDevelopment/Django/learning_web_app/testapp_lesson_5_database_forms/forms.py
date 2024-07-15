from django import forms
from testapp_lesson_4_database_admin.models import Student



class StudentForm(forms.ModelForm):

    class Meta:
        model = Student # Model this form is associated with
        fields = ['name', 'score', 'age']