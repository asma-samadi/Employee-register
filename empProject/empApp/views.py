from django.shortcuts import render

# Create your views here.
def employeeList(request):
    return render(request, 'empApp/EmployeeList.html')

def employeeForm(request):
    return render(request, 'empApp/EmployeeForm.html')

def employeeDelete(request):
    render
    