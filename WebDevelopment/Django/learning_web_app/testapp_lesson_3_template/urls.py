from django.urls import include, path
from .views import t1, t2

urlpatterns = [
    path('t1/', t1, name='name_t1'),
    path('t2/', t2, name='name_t2'),
]
