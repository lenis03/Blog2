from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Todo
from .forms import TodoCreateForm


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


def create(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(
                title=cd['title'],
                body=cd['body'],
                created=cd['created']
                )
            messages.success(request, 'Todo created successfully')
            return redirect('home:home_page')
    else:
        form = TodoCreateForm()
        
    return render(request, 'home/create.html', {'form': form})
