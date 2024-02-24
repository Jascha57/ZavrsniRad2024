from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models import Q
from django.contrib.auth.models import Group
from django.forms import model_to_dict

from users.models import CustomUser

class Event(models.Model):
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)
    thumbnail = models.ImageField(upload_to='events/', null=False, blank=False, default='events/default.png')
    title = models.CharField(max_length=100, default='Title', blank=False, null=False, unique=True)
    description = CKEditor5Field('Text', config_name='extends')
    location = models.CharField(max_length=100, default='Location', blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

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
    description = models.TextField(max_length=1000, default='Description', blank=False, null=False)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        is_new = not self.pk

        if is_new:
            Group.objects.create(name=(self.title + ' - Service'))
            self.slug = slugify(self.title)
        elif 'title' in self.get_dirty_fields():
            previous_title = Services.objects.get(pk=self.pk).title
            group = Group.objects.get(name=(previous_title + ' - Service'))
            group.name = self.title + ' - Service'
            self.slug = slugify(self.title)
            group.save()

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
    
    def get_dirty_fields(self):
        if self.pk is None:
            return {}

        original = model_to_dict(self.__class__.objects.get(pk=self.pk))
        current = model_to_dict(self)
        return {k: v for k, v in current.items() if original.get(k) != v}