from django.shortcuts import render, redirect
from .models import Todo


def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', context={'todos': todos})


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', context={'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('home:home_page')
