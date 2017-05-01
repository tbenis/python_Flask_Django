from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^destroy/(?P<id>\d+)$', views.page),
    url(r'^(?P<id>\d+)/delete$', views.delete)
]
