from django.test import TestCase
from django.contrib.auth.models import Group

from users.models import CustomUser
from website.models import Services, Schedule
from reservations.models import Reservation
from reservations.forms import *

class TestReservationForm(ReservationForm):
    # Override the captcha field with a dummy field
    captcha = forms.CharField(required=False)

class TestForms(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(email='testuser', password='12345')
        self.service = Services.objects.create(title='Test Service', description='Test Description', duration=60)
        self.doctor = CustomUser.objects.create(email='doctor', password='12345')

    # Test if the reservation form is valid when given valid data
    def test_reservationForm_valid_data(self):
        # Get a random schedule for the specific service
        self.schedule = Schedule.objects.filter(service=self.service).order_by('?').first()

        form = TestReservationForm(data={
            'user': self.user.id,
            'service': self.service.id,
            'doctor': self.doctor.id,
            'date': '2021-12-31',
            'start_time': self.schedule.start_time,
            'end_time': self.schedule.end_time,
            'description': 'Test Notes',
        })
        
        self.assertTrue(form.is_valid())

    # Test if the reservation form is invalid when given invalid data
    def test_reservationForm_invalid_data(self):
        form = TestReservationForm(data={})
        self.assertFalse(form.is_valid())
        # 4 fields are required, description is optional and captcha is not included in the form for testing
        self.assertEqual(len(form.errors), 4)