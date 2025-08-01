from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from todo.models import Task

def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)   
    #print(task)
    task.is_completed = False
    task.save()
    return redirect('home')


def edit_task(request, pk):
    get_task= get_object_or_404(Task, pk=pk)
    #print(get_task)
    if request.method=='POST':
        new_task=request.POST['task']
        #print(new_task)
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task,
        }
    
    return render(request,'edit_task.html',context)


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')