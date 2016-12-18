"""
WSGI config for django-site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""


import os
import time
import traceback
import signal
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append("/opt/python/current/app/django-site")
sys.path.append("/opt/python/run/venv/lib/python2.7/site-packages")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-site.settings")

try:
    application = get_wsgi_application()
    print 'WSGI without exception'
except Exception:
    print 'handling WSGI exception'
    # Error loading applications
    if 'mod_wsgi' in sys.modules:
        traceback.print_exc()
        os.kill(os.getpid(), signal.SIGINT)
        time.sleep(2.5)
