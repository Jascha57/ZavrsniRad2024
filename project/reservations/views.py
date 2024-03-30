from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.http import JsonResponse
from datetime import time, timedelta, date, datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import sweetify

from website.models import *
from users.models import CustomUser
from .models import *
from .forms import ReservationForm

def services(request):
    services = Services.objects.all()
    for service in services:
        group_name = service.title + ' - Service'
        service.doctors = CustomUser.objects.filter(groups__name=group_name)[:3]
    return render(request, 'services.html', {'services': services})

@login_required
def reservations(request, service_id=None):
    if request.method == 'POST':
        form = ReservationForm(request.POST)

        service_id = request.POST.get('service')
        service = get_object_or_404(Services, id=service_id)

        doctor_id = request.POST.get('doctor')
        doctor = get_object_or_404(CustomUser, id=doctor_id)

        group_name = service.title + ' - Service'
        doctors = CustomUser.objects.filter(groups__name=group_name)

        if doctor not in doctors:
            sweetify.error(request, title='Error', text='The selected doctor is not available for the selected service.', persistent='Ok')
            return render(request, 'reservations.html', {'form': form})

        form.fields['doctor'].choices = [(doctor_id, doctor_id)]
        form.fields['service'].choices = [(service_id, service_id)]

        if form.is_valid():
            doctor = form.cleaned_data['doctor']
            service = form.cleaned_data['service']
            date = form.cleaned_data['date']
            start_time = form.cleaned_data['start_time']
            description = form.cleaned_data['description']

            # Get the end time of the reservation from schedule with start time and service
            end_time = Schedule.objects.get(service=service, start_time=start_time)

            # Create the reservation
            reservation = Reservation(user=request.user, doctor=doctor, service=service, date=date, start_time=start_time, end_time=end_time.end_time, description=description)
            reservation.save()
            
            sweetify.success(request, title='Success', text='The reservation has been created.', persistent='Ok')
            return redirect('homepage')
        else:
            sweetify.error(request, title='Error', text='The form is invalid.', persistent='Ok')

    if service_id:
        if not Services.objects.filter(id=service_id).exists():
            form = ReservationForm()
        else:
            form = ReservationForm(initial={'service': service_id})
    else:
        form = ReservationForm()
    return render(request, 'reservations.html', {'form': form})

def get_doctors(request):
    service_id = request.GET.get('service')
    if not service_id:
        return JsonResponse({'error': 'Missing service_id parameter'}, status=400)
    group_name = Services.objects.get(id=service_id).title + ' - Service'
    doctors = CustomUser.objects.filter(groups__name=group_name)
    return JsonResponse(list(doctors.values('id', 'first_name', 'last_name', 'profile_picture')), safe=False)

def get_date(request):
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({'error': 'Missing date parameter'}, status=400)
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    if date < datetime.now().date():
        return JsonResponse({'valid': False})
    return JsonResponse({'valid': True})

def get_times(request):
    # Check if there are any reservations for the selected doctor on the selected date
    service_id = request.GET.get('service')
    if not service_id:
        return JsonResponse({'error': 'Missing service_id parameter'}, status=400)
    doctor_id = request.GET.get('doctor')
    if not doctor_id:
        return JsonResponse({'error': 'Missing doctor_id parameter'}, status=400)
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({'error': 'Missing date parameter'}, status=400)
    date = datetime.strptime(date_str, f'%Y-%m-%d').date()

    # Get the service's schedules
    schedules = Schedule.objects.filter(service_id=service_id)

    # Get the doctor's reservations on the selected date
    reservations = Reservation.objects.filter(doctor_id=doctor_id, date=date)

    current_time = datetime.now().time()
    current_date = datetime.now().date()

    times = []
    for schedule in schedules:
        start = schedule.start_time
        end = schedule.end_time

        # Check if the current date is the selected date and the start time is earlier than the current time
        if date == current_date and start < current_time:
            times.append({'time': f'{start}', 'filled': True})
            continue

        # Check if the time slot is reserved
        for reservation in reservations:
            if start >= reservation.start_time and end <= reservation.end_time:
                times.append({'time': f'{start}', 'filled': True})
                break
        else:
            times.append({'time': f'{start}', 'filled': False})

    return JsonResponse(times, safe=False)
    