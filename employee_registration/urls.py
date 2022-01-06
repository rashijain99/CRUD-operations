from django.contrib import admin
from django.urls import path
from django.urls.conf import include , include
from . import views

urlpatterns = [
     # first url is for employee insert   i.e get and post request for insert operation
     path('', views.e_form,  name="e_form"),

     # second url is for employee update   i.e get and post request for update operation
     path('<int:id>/', views.e_form,  name="e_update"),

     # third url is for employee list    i.e get request to retrieve and display all records
     path('list', views.e_list,  name="e_list"),

     path('delete/<int:id>/', views.e_delete,  name="e_delete"),

]
