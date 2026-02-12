from django.shortcuts import render, redirect
from .forms import Employee_form
from .models import Employee

# Create your views here.

def employeeList(request):
    employees = Employee.objects.all()
    return render(request, 'empApp/employeeList.html', {'employeeList': employees})


def employeeForm(request):
    if request.method == 'GET':
        form = Employee_form()
        return render(request, 'empApp/EmployeeForm.html', {'form':form})
    else: 
        form = Employee_form(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employeeDelete(request):
    render
    