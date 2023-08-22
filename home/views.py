from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages


def home(request):
    todos = Todo.objects.all()
    return render(request, 'home/home.html', context={'todos': todos})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'home/detail.html', context={'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'Todo deleted successfully', 'success')
    return redirect('home:home_page')
