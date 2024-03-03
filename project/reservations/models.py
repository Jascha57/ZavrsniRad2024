from django.db import models
from django.contrib.auth.models import Group
from django.db.models import Q

from users.models import CustomUser
from website.models import Services

class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_reservations')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='doctor_reservations')
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(auto_now_add=True)
    description = models.TextField(max_length=1000, default='Description', blank=False, null=False)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.user.username
    
class Schedule(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='schedules')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.service.name}: {self.start_time} - {self.end_time}'