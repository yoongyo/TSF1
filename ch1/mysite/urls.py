from django.contrib import admin
from django.conf.urls import url, include

# 미디어 설정
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^travel/', include('travel.urls', namespace='travel')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^Personalized/', include('Personalized.urls', namespace='Personalized')),
    url(r'^Booking/', include('Booking.urls', namespace='Booking')),
]




# 미디어 업로드
# 어떤 URL을 정적으로 추가할래? > MEDIA_URL을 static 파일 경로로 추가
# 실제 파일은 어디에 있는데? > MEDIA_ROOT 경로내의 파일을 static 파일로 설정

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)