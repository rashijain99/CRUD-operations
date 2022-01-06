from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django import http
from .forms import employeeForm
from .models import Employee


# get request to retrieve and display all records
def e_list(request):
    data = {
        'employeelist' : Employee.objects.all()
    }
    return render(request,'employee_list.html', data)


# get and post request for insert operation
# get and post request for update operation

def e_form(request, id=0):
    if request.method =="GET" :  # here we handle get request
        if id == 0:                 # here we handle get request for insert operation bz bydefault id=0
           fn = employeeForm()

        else:                    # here we handle get request for update operation 
            employee = Employee.objects.get(pk=id)
            fn = employeeForm(instance = employee)
        return render(request,'employee_form.html' , {'form':fn})
    


    else:                        # here we handle post request
        if id == 0:                 # here we handle post request for insert operation bz bydefault id=0
            fn = employeeForm(request.POST)  # this is form model object

        else:
            employee = Employee.objects.get(pk=id)  # employee object that have details from db
            fn = employeeForm(request.POST, instance = employee) # here data of employee object is to be updated from request.POST object data 

        # these two lines are validate for both the operations
        if fn.is_valid():
            fn.save()

        return redirect('e_list')


def e_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect("e_list")   
  