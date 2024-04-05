import datetime
from django.test import TestCase
from django.utils import timezone

from users.models import CustomUser
from django.contrib.auth.models import Group

class TestModels(TestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create(email='testuser', password='12345')
        self.group = Group.objects.create(name='Customer')
    
    def test_default_user_creation(self):
        self.assertEquals(self.user.email, 'testuser')
        self.assertEquals(self.user.profile_picture, 'default/user.jpg')
        self.assertEquals(self.user.gender, 'X')
        self.assertEquals(self.user.is_active, True)
        self.assertEquals(self.user.is_staff, False)
        self.assertEquals(self.user.is_superuser, False)