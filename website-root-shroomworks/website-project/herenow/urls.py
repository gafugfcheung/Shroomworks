from django.conf.urls import url

from . import views

app_name = 'herenow'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup/create_user$', views.create_user, name='create_user'),
    url(r'^login_screen/$', views.login_screen, name='login_screen'),
    url(r'^login_screen/login$', views.login, name='login'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^feed/$', views.feed, name='feed'),
]
