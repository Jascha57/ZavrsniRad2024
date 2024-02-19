from django.db import models
from users.models import CustomUser

class Event(models.Model):
    slug = models.SlugField(unique=True, null=False, blank=False, default='Event-Slug')
    title = models.CharField(max_length=100, default='Title', blank=False, null=False)
    description = models.TextField(default='Description', blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class News(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=False, blank=False, default='News-Slug')
    title = models.CharField(max_length=100, default='Title', blank=False, null=False)
    description = models.TextField(default='Description', blank=False, null=False)
    short_description = models.TextField(max_length=100, default='Short description', blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
