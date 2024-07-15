from django.urls import include, path
from .views import show_students_page, crud_students_page

urlpatterns = [
    path('show_students/', show_students_page),
    path('crud_students/', crud_students_page, name='submit_student_op')
]