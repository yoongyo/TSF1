from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.list, name='list'),
    url('^new/$', views.list_new, name='list_new'),
]