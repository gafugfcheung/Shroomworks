from django.contrib.auth.models import User
from herenow.models import Profile, Location, Post
from django.http import JsonResponse, HttpResponse
import json

# image processing
from django.core.files.base import ContentFile
import re
import base64


def set_profile_self(request):
    user = request.user
    if user.is_authenticated:
        profile = user.profile_set.all()[0]
        if request.is_ajax() and request.method == 'POST':
            response = json.loads(request.body.decode("utf-8"))
            user.first_name = response['firstname']
            user.last_name = response['lastname']
            user.email = response['email']
            profile.status = response['status']
            user.save()
            profile.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'invalid_request'})
    else:
        return JsonResponse({'status': 'error', 'message': 'user_not_authenticated'})


def create_post(request):
    user = request.user
    if user.is_authenticated:
        profile = user.profile_set.all()[0]
        if request.is_ajax() and request.method == 'POST':
            response = json.loads(request.body.decode("utf-8"))
            location = Location.objects.create(lat=response['lat'], lon=response['lon'])
            post = Post.objects.create(location=location, profile=profile)
            post.caption = response['caption']
            ImageData = response['image']
            dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
            ImageData = dataUrlPattern.match(ImageData).group(2)
            if ImageData is None or len(ImageData) == 0:
                return HttpResponse('Error receiving picture!')
            image_savename = user.username + post.datetime.strftime('%Y-%m-%d %H:%M') + ".jpeg"
            image = ContentFile(base64.b64decode(ImageData), image_savename)
            post.image = image
            post.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'invalid_request'})
    else:
        return HttpResponse('Invalid user', {})
