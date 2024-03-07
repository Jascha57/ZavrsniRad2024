from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('services/', views.services, name='services'),
    path('reservations/', views.reservations, name='reservations'),
    path('reservations/<int:service_id>/', views.reservations, name='reservations_with_service'),
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('get_date/', views.get_date, name='get_date'),
    path('get_times/', views.get_times, name='get_times'),
]