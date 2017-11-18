from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo

def index(request):
    todoapp = Todo.objects.all()[:10]
    context = {
         'todoapp':todoapp
    }
    return render(request,'index.html',context)
# Create your views here.
def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
         'todo':todo
    }
    return render(request,'details.html',context)

