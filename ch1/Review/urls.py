from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<title>\w+)/(?P<pk>\d+)/$', views.review, name='review'),
    url(r'^Thanks/$', views.thanks, name='thanks'),
    ]