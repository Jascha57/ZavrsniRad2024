from django.contrib import admin
from .models import *

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('title', 'date', 'description')
    readonly_fields = ('slug',)

class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ('title', 'date', 'description', 'short_description')
    readonly_fields = ('slug',)

admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)