from django.contrib import admin
from .models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'slug', 'description')
    prepopulated_fields = {'slug': ('title',)}

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'slug', 'description', 'short_description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Event)
admin.site.register(News)