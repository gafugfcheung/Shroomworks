from django.contrib.auth.models import User
from herenow.models import Profile
from django.http import JsonResponse
import json


def set_profile_self(request):
    user = request.user
    if user.is_authenticated:
        profile = user.profile_set.all()[0]
        if request.is_ajax() and request.method == 'POST':
            print 'received ajax!'
            response = json.loads(request.body.decode("utf-8"))
            user.first_name = response['firstname']
            user.last_name = response['lastname']
            user.email = response['email']
            profile.status = response['status']
            user.save()
            profile.save()
            return JsonResponse({'data': 'Profile updated!'})
