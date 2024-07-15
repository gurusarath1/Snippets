from django.urls import path
from . import views

urlpatterns = [
    path('', views.function_based_view, name='function_based_view'),
    path('class_based/', views.class_based_view.as_view(), name='class_based_view'),
    path('data_in_url/<name>/<id>', views.path_view_url_page, name='Data in url'),
    path('data_in_url_2/', views.path_view_url_page_2, name='Data in url variant 2'),
]
