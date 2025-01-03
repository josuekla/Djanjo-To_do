from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, task_description=description)

        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        task.title = title
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')