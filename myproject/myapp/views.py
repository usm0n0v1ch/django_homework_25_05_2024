from django.shortcuts import render, redirect

from myapp.models import Task


# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'myapp/task_list.html', {'tasks': tasks})

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def task_switch(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')