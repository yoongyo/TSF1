from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# WSGI application
WSGI_APPLICATION = 'mysite.config.wsgi.deploy.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db4.sqlite3'),
    }
}


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mysite', 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'mysite', 'staticfiles')
STATICFILES_DIRS = [
 os.path.join(BASE_DIR, 'static'),
]



STATICFILES_STORAGE = 'mysite.storages.StaticAzureStorage'
DEFAULT_FILE_STORAGE = 'mysite.storages.MediaAzureStorage'

AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME')
AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
    },
}