import os
from celery.signals import setup_logging
from django.conf import settings
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_afifa.settings')

app = Celery('test_afifa')

app.config_from_object('django.conf:settings', namespace='CELERY')

# run celery task in local thread, use for development and debugging
# app.conf.task_always_eager = True
# configure celery logger
@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig
    from django.conf import settings
    dictConfig(settings.LOGGING)
app.autodiscover_tasks(settings.INSTALLED_APPS)
