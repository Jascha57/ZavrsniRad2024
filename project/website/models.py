from django.db import models
from users.models import CustomUser

class Event(models.Model):
    slug = models.SlugField(unique=True, null=False, blank=False, default='Event-Slug')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class News(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=False, blank=False, default='News-Slug')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
