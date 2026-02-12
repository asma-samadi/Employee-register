from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employeeForm, name='employeeForm'),
    path('<int:id>/', views.employeeForm, name='employeeUpdate'),
    path('delete/<int:id>/', views.employeeDelete, name='employeeDelete'),
    path('list/', views.employeeList, name='employeeList'),
]  

