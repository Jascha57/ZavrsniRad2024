from django.db import models
from django.utils.text import slugify
from users.models import CustomUser
from django_ckeditor_5.fields import CKEditor5Field

class Event(models.Model):
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)
    title = models.CharField(max_length=100, default='Title', blank=False, null=False, unique=True)
    description = CKEditor5Field('Text', config_name='extends')
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
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
