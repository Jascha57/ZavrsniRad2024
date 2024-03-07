from django.contrib import admin

from .models import *

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'doctor', 'service', 'date', 'start_time', 'end_time')
    search_fields = ('user', 'doctor', 'service', 'date', 'start_time', 'end_time')

admin.site.register(Reservation, ReservationAdmin)