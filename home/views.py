from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Blog
from .forms import BlogCreateForm


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home/home.html', context={'blogs': blogs})


def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'home/detail.html', context={'blog': blog})


def delete(request, blog_id):
    Blog.objects.get(id=blog_id).delete()
    messages.success(request, 'Blog deleted successfully', 'success')
    return redirect('home:home_page')


def create(request):
    if request.method == 'POST':
        form = BlogCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Blog.objects.create(
                title=cd['title'],
                body=cd['body'],
                created=cd['created']
                )
            messages.success(request, 'Blog created successfully')
            return redirect('home:home_page')
    else:
        form = BlogCreateForm()

    return render(request, 'home/create.html', {'form': form})
