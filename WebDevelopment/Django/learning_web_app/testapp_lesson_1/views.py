from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 



# http://127.0.0.1:8000/testapp_lesson_1/?key=45
def function_based_view(request):

    if request.method == 'GET':
        val = request.GET['key']
        return HttpResponse(f"GET Request:::: This is a response form a function based view  =  {val}")

    if request.method == 'POST':
        val = request.GET['key']
        return HttpResponse(f"POST Request:::: This is a response form a function based view  = {val}")




# http://127.0.0.1:8000/testapp_lesson_1/class_based/
class class_based_view(View):

    def get(self, request):
        return HttpResponse(f"GET Request:::: This is a response form a class based view")
    
    def post(self, request):
        return HttpResponse(f"POST Request:::: This is a response form a class based view")
    



# http://127.0.0.1:8000/testapp_lesson_1/data_in_url/guru/919
def path_view_url_page(request, name, id):
    return HttpResponse(f"Path has it all <h1>{name} ---- {id}</h1>")


# http://127.0.0.1:8000/testapp_lesson_1/data_in_url_2/?name=John&id=1
def path_view_url_page_2(request):
    return HttpResponse(f"Path has it all <h1>{request.GET['name']} ---- {request.GET['id']}</h1>")