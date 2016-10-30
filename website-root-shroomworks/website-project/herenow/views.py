# http
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader

# django
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# models
from django.contrib.auth.models import User
from herenow.models import Profile, Post

# forms
from .forms import LoginForm, SignupForm

# INDEX SCREEN
def index(request):
    return render(request, 'index.html')

def index_old(request):
    return render(request, 'index_old.html')

def map(request):
    return render(request, 'map.html')


# FEED
def feed(request):
    return render(request, 'feed.html')
