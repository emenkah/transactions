from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finance.settings')

app = Celery('finance')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

