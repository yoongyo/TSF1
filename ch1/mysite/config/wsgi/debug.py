import os
import sys
from django.core.wsgi import get_wsgi_application
path = '/Users/javis/Desktop/trvel_home-master/ch1'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.config.settings.debug")

application = get_wsgi_application()

