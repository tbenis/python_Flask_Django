from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^new$', views.new),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^create$', views.create),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^destroy/(?P<id>\d+)$', views.destroy)
]
