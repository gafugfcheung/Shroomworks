# http
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader

# django
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt

# models
from herenow.models import Profile, Post
from django.contrib.auth.models import User

# forms
from .forms import LoginForm, SignupForm, UpdateProfilePictureForm, CreatePostForm, UpdateProfilePictureFormBase64

# parse image
import re
import base64
from django.core.files.base import ContentFile



# SIGN UP FUNCTIONS
def signup(request):
    form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        profile = Profile(user=user)
        profile.save()
        auth_login(request, user)
        return redirect('/herenow/profile?welcome=True')
    else:
        return HttpResponse("Error creating user! Request type not POST")


# LOGIN FUNCTION
def login(request):
    name = request.POST['username']
    pswd = request.POST['password']
    user = authenticate(username=name, password=pswd)
    if user is not None:
        auth_login(request, user)
        return redirect('/herenow/profile?welcome=True')
    else:
        return login_screen(request, '* Could not log in. Please check your username and password.')


def login_screen(request, err_msg=""):
    form = LoginForm()
    return render(request, 'login_screen.html', {'form': form, 'err_msg': err_msg})


def create_post(request, err_msg=""):
    form = CreatePostForm()
    form_pic = UpdateProfilePictureFormBase64()
    return render(request, 'new_post.html', {'form': form, 'form_pic': form_pic, 'err_msg': err_msg})


# USER PROFILE
def profile(request):
    current_user = request.user
    if current_user.is_authenticated:
        current_profile = Profile.objects.get(user=current_user)
        welcome = request.GET.get('welcome', '')
        if welcome == 'True':
            welcome = "Welcome!"
        return render_to_response('myprofile.html', {'profile': current_profile, 'welcome': welcome})
    else:
        return redirect('login_screen/')


@csrf_exempt
def logout(request):
    auth_logout(request)
    template = loader.get_template('logout_success.html')
    return HttpResponse(template.render())


@csrf_exempt
def update_status(request):
    print "> receiving status update"
    if request.is_ajax():
        print "> is_ajax() == true"
    if request.method == "POST":
        print "> method == post"
        current_user = request.user
        if current_user.is_authenticated:
            current_profile = Profile.objects.get(user=current_user)
            current_profile.status = request.POST['status']
            current_profile.save()
            return render_to_response('myprofile.html', {'profile': current_profile, 'welcome': ''})

@csrf_exempt
def update_image(request):
    current_user = request.user
    if current_user.is_authenticated:
        form = UpdateProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            current_profile = Profile.objects.get(user=current_user)
            current_profile.image.delete(save=True)
            current_profile.image = form.cleaned_data['image']
            current_profile.save()
            return render_to_response('myprofile.html', {'profile': current_profile, 'welcome': ''})
        else:
            return HttpResponse('Invalid form!')

@csrf_exempt
def update_image_base64(request):
    print 'entering update function'
    current_user = request.user
    if current_user.is_authenticated:
        dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
        ImageData = request.POST.get('image_b64')
        ImageData = dataUrlPattern.match(ImageData).group(2)
        # If none or len 0, means illegal image data
        if ImageData == None or len(ImageData) == 0:
            # PRINT ERROR MESSAGE HERE
            print "invalid size"
            pass
        # Decode the 64 bit string into 32 bit
        image = ContentFile(base64.b64decode(ImageData), current_user.username + ".jpeg")
        print 'user is authenticated'
        current_profile = Profile.objects.get(user=current_user)
        current_profile.image.delete(save=True)
        current_profile.image = image
        print 'copying data to profile'
        current_profile.save()
        print 'data saved'
        return render_to_response('myprofile.html', {'profile': current_profile, 'welcome': ''})
