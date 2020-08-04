from django.shortcuts import render
from app1.form import student

# Create your views here.

def index(request):
    name=student(request.POST)
    return render(request,"main.html",{'form':name})
