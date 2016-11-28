from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def get_ajax(request):
    html = render_to_string('herenow/test_content.html')
    return HttpResponse(html)
