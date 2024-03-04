from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('services/', views.services, name='services'),
    path('reservations/', views.reservations, name='reservations'),
    path('selected_date/', views.selected_date, name='selected_date'),
]