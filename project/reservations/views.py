from django.shortcuts import render

from website.models import Services

def services(request):
    services = Services.objects.all()
    return render(request, 'services.html', {'services': services})

def reservations(request):
    return render(request, 'reservations.html')