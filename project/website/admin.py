from django.contrib import admin
from .models import *

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('title', 'date', 'description')
    readonly_fields = ('slug',)

class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ('title', 'date', 'short_description')
    readonly_fields = ('slug',)

class ServicesAdmin(admin.ModelAdmin):
    model = Services
    list_display = ('title',)
    readonly_fields = ('slug',)

class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    list_display = ('id', 'service', 'start_time', 'end_time')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Schedule, ScheduleAdmin)