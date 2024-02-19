from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class userRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'gender', 'password1', 'password2']

    def save(self, commit=True):
        user = super(userRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user