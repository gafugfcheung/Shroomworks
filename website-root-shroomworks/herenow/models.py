from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.conf import settings


class Profile(models.Model):
    created_datetime = models.DateTimeField('date published', default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile", height_field=None, width_field=None)


class Location(models.Model):
    lat = models.DecimalField(max_digits=8, decimal_places=5)
    lon = models.DecimalField(max_digits=8, decimal_places=5)


class Post(models.Model):
    datetime = models.DateTimeField(blank=True, default=timezone.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts", height_field=None, width_field=None)