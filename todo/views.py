from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from todo.models import Task

def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')