from django.test import SimpleTestCase
from django.urls import reverse, resolve

from reservations.views import *
from website.models import Services

class TestUrls(SimpleTestCase):

    def test_services_url_resolves(self):
        url = reverse('services')
        self.assertEquals(resolve(url).func, services)

    def test_reservation_url_resolves(self):
        url = reverse('reservations')
        self.assertEquals(resolve(url).func, reservations)

    def test_reservation_with_service_url_resolves(self):
        url = reverse('reservations_with_service', args=[1])
        self.assertEquals(resolve(url).func, reservations)