from django import forms
from .models import Employee


class employeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('fullname' , 'mobile', 'emp_code' , 'position')
        labels={
            "fullname" : 'Full Name',
            "emp_code" : 'EMP.Code',
        }


    def __init__(self, *args, **kwargs):
        super(employeeForm , self).__init__(*args, **kwargs)
        self.fields['position'].empty_label ="Select"
        
  
