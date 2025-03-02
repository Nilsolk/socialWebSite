from django import forms
from django.contrib.auth.models import User
from .models import Image

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Enter Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat Password")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'description']