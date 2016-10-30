from django.conf.urls import url

from . import views
from . import profile_view

app_name = 'herenow'
urlpatterns = [
    # index
    url(r'^$', views.index, name='index'),
    url(r'^index_old/$', views.index_old, name='index_old'),

    # map
    url(r'^map/$', views.map, name='map'),
    url(r'^signup/$', profile_view.signup, name='signup'),
    url(r'^signup/create_user$', profile_view.create_user, name='create_user'),
    url(r'^login_screen/$', profile_view.login_screen, name='login_screen'),
    url(r'^login_screen/login$', profile_view.login, name='login'),

    # profile
    url(r'^profile$', profile_view.profile, name='profile'),
    url(r'^logout$', profile_view.logout, name='logout'),
    url(r'^update_status$', profile_view.update_status, name='update_status'),

    # feed
    url(r'^feed/$', views.feed, name='feed'),
]
