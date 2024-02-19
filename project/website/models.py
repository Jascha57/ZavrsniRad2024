from django.db import models
from users.models import CustomUser
from django_ckeditor_5.fields import CKEditor5Field

class Event(models.Model):
    slug = models.SlugField(unique=True, null=False, blank=False, default='')
    title = models.CharField(max_length=100, default='Title', blank=False, null=False)
    description = CKEditor5Field('Text', config_name='extends')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class News(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=False, blank=False, default='')
    title = models.CharField(max_length=100, default='Title', blank=False, null=False)
    description = CKEditor5Field('Text', config_name='extends')
    short_description = models.TextField(max_length=100, default='Short description', blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
