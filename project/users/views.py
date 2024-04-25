from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404
from encrypted_files.base import EncryptedFile
import sweetify

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
            sweetify.success(request, title='Success', text='You have successfully registered.')
            return redirect('homepage')
        else:
            sweetify.error(request, title='Error', text='Invalid form data.')
    else:
        form = userRegistrationForm()
    return render(request, 'register.html', {'form': form, "register_active": True})

@user_not_authenticated
def custom_login(request):
    if request.method == 'POST':
        form = userLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                sweetify.success(request, title='Success', text='You have successfully logged in.')
                next_url = request.GET.get('next', '/')
                return redirect(next_url)
        else:
            sweetify.error(request, title='Error', text='Invalid username or password.')
    else:
        form = userLoginForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    if request.user.is_authenticated:
        logout(request)
        sweetify.success(request, title='Success', text='You have successfully logged out.')
    else:
        sweetify.info(request, title='Info', text='You are not logged in.')
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

def download_results(request, reservation_id):
    if request.user.is_authenticated:
        reservation = get_object_or_404(Reservation, id=reservation_id)
        if reservation.user == request.user:
            if reservation.results_file:
                try:
                    response = FileResponse(EncryptedFile(reservation.results_file))
                    response['Content-Disposition'] = f'attachment; filename="results-{reservation.date}-{reservation.service}.pdf"'
                    return response
                except:
                    raise Http404()
            else:
                sweetify.error(request, title='Error', text='No results file available.')
        else:
            raise Http404()
    else:
        raise Http404()
    
def hide_results(request, path, user_id, file_name):
    if request.user.is_authenticated:
        if request.user.id == user_id:
            try:
                response = FileResponse(EncryptedFile(f'media/private/{path}/{user_id}/{file_name}'))
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                return response
            except:
                raise Http404()
        else:
            raise Http404()
    else:
        raise Http404()
    
def hide_profile_pictures(request, path, file_name):
    if request.user.is_authenticated:
        if request.user.profile_picture == f'users/{path}/{file_name}':
            try:
                response = FileResponse(request.user.profile_picture)
                return response
            except:
                raise Http404()
        else:
            raise Http404()
    else:
        raise Http404()