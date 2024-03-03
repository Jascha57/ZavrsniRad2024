from django.shortcuts import render
from django.contrib.auth.models import Group
from django.http import JsonResponse

from website.models import Services
from users.models import CustomUser

def services(request):
    services = Services.objects.all()
    for service in services:
        group_name = service.title + ' - Service'
        group = Group.objects.get(name=group_name)
        service.doctors = CustomUser.objects.filter(groups__name=group_name)
    return render(request, 'services.html', {'services': services})

def reservations(request):
    return render(request, 'reservations.html')

def selected_date(request):
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    if start_date and end_date:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})