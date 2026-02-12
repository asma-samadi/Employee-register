from django.shortcuts import render, redirect
from .forms import Employee_form
from .models import Employee

# Create your views here

def employeeForm(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = Employee_form()
        else:
            employee = Employee.objects.get(pk=id)
            form = Employee_form(instance=employee)

        return render(request, 'empApp/EmployeeForm.html', {'form':form})
    else: 
        if id == 0:
            form = Employee_form(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = Employee_form(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
    
def employeeList(request):
    employees = Employee.objects.all()
    return render(request, 'empApp/employeeList.html', {'employeeList': employees})

def employeeDelete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')