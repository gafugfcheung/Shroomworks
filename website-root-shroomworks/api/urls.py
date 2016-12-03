from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'herenow'
urlpatterns = [

    # ajax
    url(r'^validate_username/$', views.validate_username, name='validate_username'),
    url(r'^get_ajax/$', views.get_ajax, name='get_ajax'),
    url(r'^get_profile_self/$', views.get_profile_self, name='get_profile_self'),
    url(r'^get_profile/(?P<pk>[0-9]+)/$', views.get_profile, name='get_profile'),
    url(r'^get_post/(?P<pk>[0-9]+)/$', views.get_post, name='get_post'),
    url(r'^get_post_all/$', views.get_post_all, name='get_post_all'),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
