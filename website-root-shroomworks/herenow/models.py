from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.conf import settings


class Profile(models.Model):
    created_datetime = models.DateTimeField('date published', default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profile", height_field=None, width_field=None, default='profile/default.jpeg')


class Location(models.Model):
    lat = models.DecimalField(max_digits=8, decimal_places=5)
    lon = models.DecimalField(max_digits=8, decimal_places=5)
    description = models.CharField(max_length=100)


class Post(models.Model):
    datetime = models.DateTimeField(blank=True, default=timezone.now)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location')
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts", height_field=None, width_field=None)

    def time_elapsed(self):
        timedelta = timezone.now() - self.datetime
        seconds = timedelta.seconds
        minutes = seconds/60
        hours = minutes/60
        minutes = minutes - hours*60
        days = timedelta.days
        if days > 0:
            return str(days) + ' days and ' + str(hours) + ' hours ago'
        elif hours > 0:
            return str(hours) + ' hours and ' + str(minutes) + ' minutes ago'
        elif minutes > 0:
            return str(minutes) + ' minutes ago'
        else:
            return 'Just now'
