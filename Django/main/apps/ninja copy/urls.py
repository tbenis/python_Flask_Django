from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^ninjas/(?P<ninja_color>\w+)$', views.show)
    # url(r'^ninjas/(?P<ninja_color>[a-z]+)$', views.show)
]
