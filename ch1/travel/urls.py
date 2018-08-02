from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$', views.main, name='main'),
    url(r'^local/$', views.local_list, name="local_list"),
    url(r'^local/(?P<City>\w+)/$', views.local_detail, name="local_detail"),
    url(r'^local/(?P<City>\w+)/(?P<pk>\d+)/$', views.local_detail_form, name='local_detail_form'),
    url(r'^local/(?P<City>\w+)/(?P<pk>\d+)/booking/$', views.booking, name="booking"),
    url(r'^local/(?P<City>\w+)/(?P<pk>\d+)/booking/complete/$', views.bookingcomplete, name="bookingcomplete"),
    url(r'^new/$', views.post_new, name="post_new"),
    url(r'^local/(?P<City>\w+)/(?P<pk>\d+)/edit/$', views.post_edit, name="post_edit"),
    url(r'^new/complete/$', views.postcomplete, name="complete"),
]


