from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pic_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(add)/$', views.add),
]
