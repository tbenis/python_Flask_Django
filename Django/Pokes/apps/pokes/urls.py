from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^rProcess$', views.rProcess),
    url(r'^success$', views.success),
    url(r'^lProcess$', views.lProcess),
    


]
