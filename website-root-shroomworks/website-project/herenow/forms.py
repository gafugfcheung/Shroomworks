from .models import Profile
from django import forms
from django.db import models
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class UpdateProfilePictureForm(forms.Form):
    image = forms.ImageField()

class UpdateProfilePictureFormBase64(forms.Form):
    image_b64 = forms.CharField()

class CreatePostForm(forms.Form):
    image = forms.ImageField()
    caption = forms.CharField(label='Caption', max_length=100)
    lat = forms.DecimalField(max_digits=8, decimal_places=5)
    lon = forms.DecimalField(max_digits=8, decimal_places=5)
