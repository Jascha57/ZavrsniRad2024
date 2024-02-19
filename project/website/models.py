from django.db import models
from users.models import CustomUser

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class News(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
