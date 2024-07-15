from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path('page_1/', views.database_page_1), 
]
