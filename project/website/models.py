from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models import Q
from django.contrib.auth.models import Group
from django.forms import model_to_dict
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import time, datetime, timedelta, date

from users.models import CustomUser

class Event(models.Model):
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)
    thumbnail = models.ImageField(upload_to='events/', null=False, blank=False, default='events/default.png')
    title = models.CharField(max_length=100, default='Title', blank=False, null=False, unique=True)
    description = CKEditor5Field('Text', config_name='extends')
    location = models.CharField(max_length=100, default='Location', blank=False, null=False)
    date = models.DateTimeField()
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class News(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to=Q(is_staff=True) | Q(is_superuser=True))
    thumbnail = models.ImageField(upload_to='news/', null=False, blank=False, default='news/default.png')
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)
    title = models.CharField(max_length=100, default='Title', blank=False, null=False, unique=True)
    description = CKEditor5Field('Text', config_name='extends')
    short_description = models.TextField(max_length=100, default='Short description', blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Services(models.Model):
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)
    title = models.CharField(max_length=100, default='Title', blank=False, null=False, unique=True)
    description = CKEditor5Field('Text', config_name='extends')
    duration = models.IntegerField(default=30, blank=False, null=False, help_text='Duration in minutes')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        is_new = not self.pk
        interval_changed = False

        if is_new:
            Group.objects.create(name=(self.title + ' - Service'))
        else:
            if 'title' in self.get_dirty_fields():
                previous_title = Services.objects.get(pk=self.pk).title
                group = Group.objects.get(name=(previous_title + ' - Service'))
                group.name = self.title + ' - Service'
                group.save()

            if 'duration' in self.get_dirty_fields():
                interval_changed = True

        super().save(*args, **kwargs)

        if is_new or interval_changed:
            create_schedules_for_service(self)
    
    def get_dirty_fields(self):
        if self.pk is None:
            return {}

        original = model_to_dict(self.__class__.objects.get(pk=self.pk))
        current = model_to_dict(self)
        return {k: v for k, v in current.items() if original.get(k) != v}
    
def create_schedules_for_service(service):
    # Delete old schedules if they exist
    service.schedules.all().delete()

    # Create new schedules
    start_time = time(hour=7)
    end_time = time(hour=21)

    current_time = start_time
    while current_time < end_time:
        start = current_time
        end = (datetime.combine(date.min, current_time) + timedelta(minutes=service.duration)).time()
        Schedule.objects.create(service=service, start_time=start, end_time=end)
        current_time = end
    
class Schedule(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='schedules')
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'

    def __str__(self):
        return f'{self.service.title}: {self.start_time} - {self.end_time}'