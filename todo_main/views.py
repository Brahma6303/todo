#from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task
def home(request):
    #return HttpResponse("<h1>Welcome to home page</h1>")
    tasks=Task.objects.filter(is_completed=False).order_by('-updated_at')
    #print(tasks)
    completed_tasks=Task.objects.filter(is_completed=True).order_by('-updated_at')
    print(completed_tasks)
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request,'home.html',context)