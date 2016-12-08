from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from herenow.models import Post
from django.core import serializers
# Create your views here.

from rest_framework import viewsets
from api.serializers import UserSerializer, PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-datetime')
    serializer_class = PostSerializer
