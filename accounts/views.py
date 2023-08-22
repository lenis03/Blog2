from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserRegistrationForm


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                cd['user_name'],
                cd['email'],
                cd['password']
                )
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            messages.success(request, 'User created successfully.', 'success')
            return redirect('home:blog_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})          
