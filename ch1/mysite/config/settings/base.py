import os
import uuid
from datetime import datetime
import json
from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

BASE1_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)

# .config_secret 폴더 및 하위 파일 경로
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secrets')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
CONFIG_SECRET_DEBUG_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_debug.json')
CONFIG_SECRET_DEPLOY_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_deploy.json')

config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())

SECRET_KEY = config_secret_common['django']['secret_key']



ALLOWED_HOSTS = []




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'travel',
    'accounts',
    'Booking',
    'Personalized',
    'Review',
    'imagekit',
    'django_select2',
    # 로그인 부분
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.kakao',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# 로그인 부분
AUTHENTICTION_BACKEDS=[
    'django.contrib.auth.backends.ModelBackend',            # 기본 인증 백엔드
    'allauth.account.auth_backends.AuthenticationBacked',   # 추가
]

# 로그인 부분
# 등록하지 않으면, 각 요청 시에 host 명의 인스턴스를 찾습니다.
SITE_ID = 1

# 로그인 부분
# 이메일 확인을 하지 않음
SOCIALACCOUNT_EMAIL_VERIFICATION ='none'

# 로그인 부분
# 기본 로그인 페이지 URL 을 지정
# login_required 장식자 등에 의해서 사용

from django.urls import reverse_lazy

LOGIN_URL = reverse_lazy('login')

LOGIN_URL = '/accounts/login/'
# 로그인 완료 후에 next 인자가 지정되면 해당 URL 로 페이지 이동
# next 인자가 없으면 본 URL 로 이동
LOGIN_REDIRECT_URL = '/accounts/profile/'
# 로그아웃 완료 후에
# - next_page 인자가 지정되면 next_page URL 로 페이지 이동
# - next_page 인자가 없으면 LOGOUT_REDIRECT_URL 이 지정되었을 경우 해당 URL로 이동
# - next_page 인자가 지정되지 않고 LOGOUT_REDIRECT_URL이 None일 경우
# redirect를 수행하지 않고 'registration/logged_out.html' 템플릿 렌더링
LOGOUT_REDIRECT_URL = None
# 인증에 사용할 커스텀 User 모델 지정, '앱이름.모델명'
#



AUTH_USER_MODEL = 'auth.User'




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

NAVER_CLIENT_ID = '08EHhkPy8yFmFkD4jQxm'

# 스케줄

# 이메일 보내기
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

GOOGLE_API_KEY = 'AIzaSyBJlyU9z-Iw3444-WAiDYPHNc-fKsj51Bc'
