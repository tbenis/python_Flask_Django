from django.conf.urls import url, include
from . import  views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.addd),
    url(r'^addf$', views.addf),
]
