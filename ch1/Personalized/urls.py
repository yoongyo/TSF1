from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^newPersonalized/$', views.list_new, name='list_new'),
    url(r'^(?P<pk>\d+)/personaledit/$', views.personalized_edit, name='Personalized_edit'),
    url(r'^(?P<pk>\d+)/new/$', views.new, name='new'),
    url(r'^complete/$', views.complete, name='complete'),
    url(r'^(?P<pk>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<pk>\d+)/$', views.detail, name="detail"),
]