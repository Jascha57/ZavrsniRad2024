from django.test import TestCase, Client
from django.urls import reverse

from users.views import *

class TestViews(TestCase):
    
        def setUp(self):
            self.client = Client()
            user = CustomUser.objects.create_user(email='testuser', password='12345')
            staff_user = CustomUser.objects.create_user(email='staffuser', password='12345', is_staff=True, is_superuser=False)
            admin_user = CustomUser.objects.create_user(email='adminuser', password='12345', is_staff=True, is_superuser=True)
            self.login_url = reverse('login')
            self.logout_url = reverse('logout')
            self.register_url = reverse('register')
            self.profile_url = reverse('profile')
            self.admin_url = reverse('admin:index')

        # Testing when the user is not logged in
        def test_login_GET_not_logged_in(self):
            self.client.logout()
            response = self.client.get(self.login_url)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'login.html')

        def test_logout_GET_not_logged_in(self):
            self.client.logout()
            response = self.client.get(self.logout_url)
            self.assertEquals(response.status_code, 302)

        def test_register_GET_not_logged_in(self):
            self.client.logout()
            response = self.client.get(self.register_url)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'register.html')

        def test_profile_GET_not_logged_in(self):
            self.client.logout()
            response = self.client.get(self.profile_url)
            self.assertEquals(response.status_code, 302)
            self.assertRedirects(response, '/login/?next=/profile/')

        def test_admin_GET_not_logged_in(self):
            self.client.logout()
            response = self.client.get(self.admin_url)
            self.assertEquals(response.status_code, 404)

        # Testing when the user is logged in
        def test_login_GET_logged_in(self):
            self.client.login(email='testuser', password='12345')
            response = self.client.get(self.login_url)
            self.assertEquals(response.status_code, 302)
            self.assertRedirects(response, '/')

        def test_logout_GET_logged_in(self):
            self.client.login(email='testuser', password='12345')
            response = self.client.get(self.logout_url)
            self.assertEquals(response.status_code, 302)
            self.assertRedirects(response, '/')

        def test_register_GET_logged_in(self):
            self.client.login(email='testuser', password='12345')
            response = self.client.get(self.register_url)
            self.assertEquals(response.status_code, 302)
            self.assertRedirects(response, '/')

        def test_profile_GET_logged_in(self):
            self.client.login(email='testuser', password='12345')
            response = self.client.get(self.profile_url)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'profile.html')

        # Testing when the user is logged in but not staff
        def test_admin_GET_logged_in_not_staff(self):
            self.client.login(email='testuser', password='12345')
            response = self.client.get(self.admin_url)
            self.assertEquals(response.status_code, 404)

        # Testing when the user is logged in and is staff
        def test_admin_GET_logged_in_staff(self):
            self.client.login(email='staffuser', password='12345')
            response = self.client.get(self.admin_url)
            self.assertEquals(response.status_code, 200)

        # Testing when the user is logged in and is admin
        def test_admin_GET_logged_in_admin(self):
            self.client.login(email='adminuser', password='12345')
            response = self.client.get(self.admin_url)
            self.assertEquals(response.status_code, 200)
