from django.test import TestCase, Client
from django.urls import reverse

from reservations.views import *
from website.models import Services

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(email='testuser', password='12345')
        self.services_url = reverse('services')
        self.reservations_url = reverse('reservations')
        self.service = Services.objects.create(title='Test Service', description='Test Description', duration=60)
        self.reservations_with_service_url = reverse('reservations_with_service', args=[self.service.id])

    def test_services_GET(self):
        response = self.client.get(self.services_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'services.html')

    # When the user is not logged in, the user should be redirected to the login page
    def test_reservations_GET_not_logged_in(self):
        self.client.logout()
        response = self.client.get(self.reservations_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, f'/login/?next=/reservations/')

    def test_reservations_with_service_GET_not_logged_in(self):
        self.client.logout()
        response = self.client.get(self.reservations_with_service_url)
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, f'/login/?next=/reservations/{self.service.id}/')

    # When the user is logged in, the user should be able to access the reservations page
    def test_reservations_GET_logged_in(self):
        self.client.login(email='testuser', password='12345')
        response = self.client.get(self.reservations_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations.html')

    def test_reservations_with_service_GET_logged_in(self):
        self.client.login(email='testuser', password='12345')
        response = self.client.get(self.reservations_with_service_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations.html')