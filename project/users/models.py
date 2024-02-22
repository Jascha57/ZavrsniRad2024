from django.db import models
from django.contrib.auth.models import AbstractUser
import os

from .managers import CustomUserManager

class CustomUser(AbstractUser):

    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Users", self.username, instance)
        return None

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Other'),   
    )

    username = None
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='X')
    profile_picture = models.ImageField(default='default/user.jpg', upload_to=image_upload_to)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email