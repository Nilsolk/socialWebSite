from django import forms
from django.contrib.auth.models import User
from .models import Image
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Enter Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat Password")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'description']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']