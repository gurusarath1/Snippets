from django.shortcuts import render
from django.http import HttpResponse


# http://127.0.0.1:8000/
def index(request):
    return HttpResponse("Hi all! This is a base app view")
