from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from herenow.models import Post
from django.core import serializers


def get_profile_self(request):
    user = request.user
    if user.is_authenticated:
        profile = user.profile_set.all()
        profile = profile[0]
        data = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'status': profile.status,
            'image': profile.image.url
        }
        return JsonResponse(data)
