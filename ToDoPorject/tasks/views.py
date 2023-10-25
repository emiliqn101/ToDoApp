from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse



def index(request):
    tasks = Task.objects.all()
    
    context = {'tasks':tasks}
    
    return render(request, 'tasks/list.html', context)

def create_task(request):
    if request.method == "POST":
        task_name = request.POST.get('task_name')
        if task_name:
            # Check if a task with the same name already exists
            existing_task = Task.objects.filter(title=task_name).first()
            if existing_task:
                return JsonResponse({'message': 'Task with the same name already exists.'})
            else:
                task = Task.objects.create(title=task_name)
                return JsonResponse({'message': 'Task created successfully.'})
        else:
            return JsonResponse({'message': 'Task name cannot be empty.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'})
    
def change_state(request):
    if request.method == "POST":
        task_name = request.POST.get('taskname')  # Change 'taskname' to 'task_name'
        completed = request.POST.get('completed')
    if task_name and completed:
        try:
            task = Task.objects.get(title=task_name)
            task.complete = completed.lower() == 'true'
            task.save()
            return JsonResponse({'message': 'Task state updated successfully.'})
        except Task.DoesNotExist:
            return JsonResponse({'message': 'Task not found.'})
    else:
        return JsonResponse({'message': 'Invalid data provided.'})
    
def delete_task(request):
    if request.method == "POST":
        task_name = request.POST.get('taskname')  # Change 'taskname' to 'task_name'
    if task_name:
        try:
            task = Task.objects.get(title=task_name)
            task.delete()
            return JsonResponse({'message': 'Task deleted successfully.'})
        except Task.DoesNotExist:
            return JsonResponse({'message': 'Task not found.'})
    else:
        return JsonResponse({'message': 'Invalid data provided.'})