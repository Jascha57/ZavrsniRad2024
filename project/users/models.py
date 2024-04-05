from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

from .managers import CustomUserManager

class CustomUser(AbstractUser):

    def image_upload_to(self, filename):
        return 'users/user_{0}/{1}'.format(self.id, filename)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Not Specified'),
    )

    username = None
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='X')
    profile_picture = models.ImageField(default='default/user.jpg', upload_to=image_upload_to, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.profile_picture:
            self.profile_picture = 'default/user.jpg'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email