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

    def __init__(self, *args, **kwargs):
        super(Employee_form,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'