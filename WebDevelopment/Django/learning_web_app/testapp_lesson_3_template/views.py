from django.shortcuts import render

# http://127.0.0.1:8000/testapp_lesson_3/t1/
def t1(request):

    return render(request, 't1.html')

# http://127.0.0.1:8000/testapp_lesson_3/t2/
def t2(request):

    dict_to_html = {'var1': 998, 'var2': 'Hare Krishna!!'}

    return render(request, 't2.html', dict_to_html)