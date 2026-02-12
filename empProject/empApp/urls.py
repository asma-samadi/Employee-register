from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employeeForm, name='employeeForm'),
    path('list/', views.employeeList, name='employeeList'),
]  
