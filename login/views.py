from django.shortcuts import render
from django import template
from .forms import SchoolForm
from .forms import StudentForm 

def index(request): 
    return render (request, 'index.html')

def schooladmin(request): 
    return render (request, 'school-admin.html')

def datastatement(request): 
    return render (request, 'data-statement.html')

def browse(request): 
    return render (request, 'browse.html')

def about(request): 
    return render (request, 'about.html')

def showformschool(request):
    form= SchoolForm(request.POST or None)
    if form.is_valid():
        form.save() 
    render(request, 'school-signup.html')
  
    context= {'form': form }

def showformstudent(request): 
    formstudent = StudentForm(request.POST or None)
    if formstudent.is_valid(): 
        formstudent.save() 
    
