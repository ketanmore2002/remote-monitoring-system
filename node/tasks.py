# your_app/tasks.py

from celery import shared_task
from datetime import datetime, time, timedelta
from node.models import water_tank_records_temp
from django.utils import timezone

@shared_task(bind=True)
def delete_objects_task(self):
    water_tank_records_temp.objects.all().delete()
    # print("Objects deleted successfully.")
    return f'{datetime.now()}: Objects deleted successfully.'

# @shared_task
# def schedule_delete_objects_task():
#     print("running !.")
#     scheduled_time = time(hour=14, minute=30)
#     now = timezone.now().time()

#     if now >= scheduled_time:
#         delete_objects_task().delay()

#     next_run = datetime.combine(datetime.now() + timedelta(days=1), scheduled_time)
#     return f'Next run: {next_run}'
 
# start worker : celery -A water_tank_system worker --loglevel=info
# start beat  : celery -A water_tank_system beat -l info