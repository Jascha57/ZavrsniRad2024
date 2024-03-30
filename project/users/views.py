from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group

from .forms import *
from .decorators import *
from reservations.models import *

@user_not_authenticated
def register(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group, created = Group.objects.get_or_create(name='Customer')
            user.groups.add(group)
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
                next_url = request.GET.get('next', '/')
                return redirect(next_url)
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

@login_required
def profile(request):
    if request.user.is_staff:
        # Check if the user is a part of a group with "Service" in the name
        if request.user.groups.filter(name__icontains='Service').exists():
            # Return all reservations where the user is the doctor
            reservations = Reservation.objects.filter(doctor=request.user)
        else:
            # Return all reservations where the user is the patient
            reservations = Reservation.objects.filter(user=request.user)
    else:
        reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'profile.html', context={
        'reservations': reservations,
    })