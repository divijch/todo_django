from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from . models import Task

def addtask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')
