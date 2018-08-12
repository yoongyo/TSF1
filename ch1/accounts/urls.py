from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={'next_page': settings.LOGIN_URL}),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^newprofile/$', views.new_profile, name='new_profile'),
    url(r'^newprofile/edit/$', views.profileEdit, name="profileEdit"),
    url(r'^country', views.country, name="country")
]