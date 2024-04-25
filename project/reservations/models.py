from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.files.storage import default_storage

from users.models import CustomUser
from website.models import Services

class Reservation(models.Model):
    def file_upload_to(self, filename):
        new_filename = 'results-{0}-{1}.pdf'.format(self.date, self.service)
        return 'private/results/{0}/{1}'.format(self.user.id, new_filename)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_reservations')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='doctor_reservations')
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(max_length=1000, default='', blank=True)
    results_file = models.FileField(upload_to=file_upload_to, null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    # Deletes the file if neccessary
    def save(self, *args, **kwargs):
        if self.pk and not self.results_file:
            old = Reservation.objects.get(pk=self.pk)
            if old.results_file:
                default_storage.delete(old.results_file.path)

        super().save(*args, **kwargs)