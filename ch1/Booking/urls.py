from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.booking, name='booking'),
    url(r'^complete$', views.complete, name='complete')
]