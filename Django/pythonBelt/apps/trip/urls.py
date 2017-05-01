# APP URLS

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^rProcess$', views.rProcess),
    url(r'^success$', views.success),
    url(r'^lProcess$', views.lProcess),
    url(r'^dash$', views.dash),
    url(r'^addplan$', views.addplan),
    url(r'^tripinfo$', views.tripinfo),
    url(r'^showtrip$', views.showtrip),
    url(r'^clear$', views.clear),

]
