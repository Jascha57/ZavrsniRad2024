from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class userRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'gender', 'password1', 'password2']

    def save(self, commit=True):
        user = super(userRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class userLoginForm(AuthenticationForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']