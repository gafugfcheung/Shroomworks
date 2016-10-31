from django.conf.urls import url

from . import views
from . import profile_view

from django.conf import settings
from django.conf.urls.static import static

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
    url(r'^update_image$', profile_view.update_image, name='update_image'),
    url(r'^new_post/update_image_base64$', profile_view.update_image_base64, name='update_image_base64'),

    # feed
    url(r'^feed/$', views.feed, name='feed'),

    # post
    url(r'^new_post/$', profile_view.create_post, name='new_post'),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
