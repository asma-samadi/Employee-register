from django import forms
from .models import Employee

class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('full_Name', 'mobile', 'email', 'position')
        lables = {
            'full_Name': 'Full Name',
            'mobile': 'Mobile',
            'email': 'Email',
            'position': 'Position',
        }