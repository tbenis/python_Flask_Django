from django.conf.urls import url
from . import views

#Models -- Veiws -- Templates

urlpatterns = [
  url(r'^$', views.index)
]
