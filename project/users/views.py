from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from .decorators import *

@user_not_authenticated
def register(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully registered.")
            return redirect('homepage')
        else:
            print(form.errors)
    else:
        form = userRegistrationForm()
    return render(request, 'register.html', {'form': form})

@user_not_authenticated
def custom_login(request):
    if request.method == 'POST':
        form = userLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in.")
                return redirect('homepage')
        else:
            print(form.errors)
    else:
        form = userLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def custom_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('homepage')