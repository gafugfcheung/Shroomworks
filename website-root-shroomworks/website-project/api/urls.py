from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'herenow'
urlpatterns = [

    # ajax
    url(r'^validate_username/$', views.validate_username, name='validate_username'),
    url(r'^get_ajax/$', views.get_ajax, name='get_ajax'),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
