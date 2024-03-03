from django.shortcuts import render
from django.contrib.auth.models import Group
from django.http import JsonResponse
from datetime import time, timedelta, date, datetime

from website.models import Services
from users.models import CustomUser

def services(request):
    services = Services.objects.all()
    for service in services:
        group_name = service.title + ' - Service'
        service.doctors = CustomUser.objects.filter(groups__name=group_name)
    return render(request, 'services.html', {'services': services})

def reservations(request):
    start_time = time(hour=7)
    end_time = time(hour=21)
    time_slots = []

    current_time = start_time
    while current_time <= end_time:
        time_slots.append(current_time)
        current_time = (datetime.combine(date.min, current_time) + timedelta(minutes=30)).time()

    return render(request, 'reservations.html', {'time_slots': time_slots})

def selected_date(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    if start_date and end_date:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})