from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

class Pic(models.Model):
    lat = models.FloatField(default=0.0)
    lng = models.FloatField(default=0.0)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False)
