from django.contrib import admin
from django.utils.html import format_html

from .models import *

# CUSTOM ACTIONS

@admin.action(description='Unpublish selected news or events')
def unpublish(modeladmin, request, queryset):
    queryset.update(published=False)
@admin.action(description='Publish selected news or events')
def publish(modeladmin, request, queryset):
    queryset.update(published=True)

class EventAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('title', 'date', 'published')
    readonly_fields = ('slug', 'display_thumbnail')
    fields = ('thumbnail', 'display_thumbnail', 'title', 'description', 'location', 'date', 'published')
    actions = [unpublish, publish]

    def display_thumbnail(self, obj):
        return format_html('<img src="{}" width="300" height="300" class="img-fluid" />', obj.thumbnail.url)
    display_thumbnail.short_description = 'Thumbnail Preview'

class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ('title', 'date', 'published')
    readonly_fields = ('slug', 'display_thumbnail', 'date')
    fields = ('author', 'thumbnail', 'display_thumbnail', 'title', 'description', 'short_description', 'published')
    actions = [unpublish, publish]

    def display_thumbnail(self, obj):
        return format_html('<img src="{}" width="300" height="300" class="img-fluid" />', obj.thumbnail.url)
    display_thumbnail.short_description = 'Thumbnail Preview'

class ServicesAdmin(admin.ModelAdmin):
    model = Services
    list_display = ('title',)
    readonly_fields = ('slug',)

class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    list_display = ('id', 'service', 'start_time', 'end_time')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Event, EventAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Schedule, ScheduleAdmin)