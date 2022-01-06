from django.db import models

# Create your models here.

class position(models.Model):
    title = models.CharField(max_length=50)


# we are creating this function because in form it is showing table objects, rather then its values. So to display the values of db in form we use this function.
    def __str__(self):
        return self.title
    


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code= models.CharField(max_length=5)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(position , on_delete=models.CASCADE)


  

