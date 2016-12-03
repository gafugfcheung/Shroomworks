from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from herenow.models import Post
from django.core import serializers
# Create your views here.

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def get_ajax(request):
    html = render_to_string('test_content.html')
    return HttpResponse(html)

def get_profile_self(request):
    current_user = request.user
    if current_user.is_authenticated:
        return get_profile(request, current_user.pk)

def get_profile(request, pk):
    user = User.objects.get(pk=pk)
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


def get_post(request, pk):
    post = Post.objects.get(pk=pk)
    data = {
        'caption': post.caption,
        'image': post.image.url
    }
    return JsonResponse(data)


def get_post_all(request):
    leads_as_json = serializers.serialize('json', Post.objects.all())
    return HttpResponse(leads_as_json, content_type='json')




# def get_post_all(request):
#     posts = Post.objects.all()
#     ls = []
#     for p in posts:
#         data = {
#             'caption': p.caption,
#             'image': p.image.url
#         }
#         ls.append(data)
#     return JsonResponse(ls)
