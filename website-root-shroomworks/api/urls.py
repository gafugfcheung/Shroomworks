from django.conf.urls import url, include

from . import views_get
from . import views_set
from . import views_rest

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views_rest.UserViewSet)
router.register(r'posts', views_rest.PostViewSet)


app_name = 'herenow'
urlpatterns = [

    # ajax
    url(r'^get_profile_self/$', views_get.get_profile_self, name='get_profile_self'),
    url(r'^set_profile_self$', views_set.set_profile_self, name='set_profile_self'),

    # rest framework
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
