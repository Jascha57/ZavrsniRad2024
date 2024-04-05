from django.test import TestCase

from users.models import CustomUser
from users.forms import *

class TestUserRegistrationForm(userRegistrationForm):
    # Override the captcha field with a dummy field
    captcha = forms.CharField(required=False)

class TestForms(TestCase):

    def setUp(self):
        # Create a user
        CustomUser.objects.create_user('john.doe2@gmail.com', 'password123')

    # Test if the user registration form is valid when given valid data
    def test_userRegistrationForm_valid_data(self):
        form = TestUserRegistrationForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@gmail.com',
            'gender': 'M',
            'password1': 'thisShouldBeAValidPassword9137843',
            'password2': 'thisShouldBeAValidPassword9137843',
        })

        self.assertTrue(form.is_valid())

    # Test if the user registration form is invalid when given an existing email
    def test_userRegistrationForm_existing_email(self):
        form = TestUserRegistrationForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe2@gmail.com',
            'gender': 'M',
            'password1': 'thisShouldBeAValidPassword9137843',
            'password2': 'thisShouldBeAValidPassword9137843',
        })

        self.assertFalse(form.is_valid())

    # Test if the user registration form is invalid when given an invalid email
    def test_userRegistrationForm_invalid_email(self):
        form = TestUserRegistrationForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe',
            'gender': 'M',
            'password1': 'thisShouldBeAValidPassword9137843',
            'password2': 'thisShouldBeAValidPassword9137843',
        })

        self.assertFalse(form.is_valid())

    # Test if the user registration form is invalid when the password is weak
    def test_userRegistrationForm_weak_password(self):
        form = TestUserRegistrationForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@gmail.com',
            'gender': 'M',
            'password1': '1234',
            'password2': '1234',
        })

        self.assertFalse(form.is_valid())

    # Test if the user registration form is invalid when the passwords do not match
    def test_userRegistrationForm_passwords_do_not_match(self):
        form = TestUserRegistrationForm(data={
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@gmail.com',
            'gender': 'M',
            'password1': 'thisShouldBeAValidPassword9137843',
            'password2': 'thisShouldBeAnInValidPassword9137843',
        })

        self.assertFalse(form.is_valid())

    # Test when no data is given
    def test_userRegistrationForm_no_data(self):
        form = TestUserRegistrationForm(data={})

        self.assertFalse(form.is_valid())