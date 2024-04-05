from django.test import SimpleTestCase
from django.urls import reverse, resolve

from users.views import *

class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, custom_login)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, custom_logout)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)