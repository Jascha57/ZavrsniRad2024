from django.db import models

from users.models import CustomUser
from website.models import Services

class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_reservations')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='doctor_reservations')
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(max_length=1000, default='', blank=False, null=False)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name