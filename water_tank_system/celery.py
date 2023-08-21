from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'water_tank_system.settings')

app = Celery('water_tank_system')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

app.conf.broker_url = 'redis://localhost:6379'  # Update with your Redis configuration
app.conf.result_backend = 'redis://localhost:6379'
app.conf.broker_connection_retry_on_startup = True

app.conf.beat_schedule = {
    'refresh-everyday-at-12AM' :{
        'task' : 'node.tasks.delete_objects_task',
        'schedule' : crontab(hour = 23 , minute = 42)
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")