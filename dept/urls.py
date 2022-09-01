from django.contrib import admin
from django.urls import path
from dept import views

urlpatterns = [
    path("",views.index,name='index'),
    path("",views.emp,name='emp')
]
