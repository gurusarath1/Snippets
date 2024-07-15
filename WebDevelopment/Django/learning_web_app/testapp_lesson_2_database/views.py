from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicationForm 

# http://127.0.0.1:8000/testapp_lesson_2/page_1/
def database_page_1(request):

    form = ApplicationForm() 

    return render(request, 'form.html', {'form': form}) 

