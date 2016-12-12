from .models import Profile
from django import forms
from django.db import models
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class UpdateProfilePictureForm(forms.Form):
    image = forms.ImageField()


class UpdateProfilePictureFormBase64(forms.Form):
    image_b64 = forms.CharField(widget=forms.HiddenInput())


class CreatePostForm(forms.Form):
    image_b64 = forms.CharField()
    caption = forms.CharField(label='Caption', max_length=100)
    lat = forms.DecimalField()
    lon = forms.DecimalField()


class TestForm(forms.Form):
    test_field = forms.CharField(label='test_field', max_length=100)
