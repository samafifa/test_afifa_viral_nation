import os

from django.conf import settings
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_afifa.settings')

app = Celery('test_afifa')

app.config_from_object('django.conf:settings', namespace='CELERY')

# run celery task in local thread, use for development and debugging
# app.conf.task_always_eager = True

app.autodiscover_tasks(settings.INSTALLED_APPS)
