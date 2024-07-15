"""learning_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from baseapp import views as baseapp_views

urlpatterns = [
    path('', include('baseapp.urls')), 
    path('testapp_lesson_1/', include('testapp_lesson_1.urls')), 
    path('testapp_lesson_2/', include('testapp_lesson_2_database.urls')), 
    path('testapp_lesson_3/', include('testapp_lesson_3_template.urls')), 
    path('testapp_lesson_5/', include('testapp_lesson_5_database_forms.urls')), 
    path('admin/', admin.site.urls),
]
