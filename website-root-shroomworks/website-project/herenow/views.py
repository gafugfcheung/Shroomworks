from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


from .forms import LoginForm, SignupForm


# INDEX SCREEN
def index(request):
    return render(request, 'index.html')


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


# USER PROFILE
def profile(request):
    current_user = request.user
    if current_user.is_authenticated:
        welcome = request.GET.get('welcome', '')
        if welcome == 'True':
            welcome = "Welcome!"
        return render_to_response('myprofile.html', {'user': current_user, 'welcome': welcome})
    else:
        return redirect('login_screen/')


@csrf_exempt
def logout(request):
    auth_logout(request)
    template = loader.get_template('logout_success.html')
    return HttpResponse(template.render())


# FEED
def feed(request):
    return render(request, 'feed.html')
