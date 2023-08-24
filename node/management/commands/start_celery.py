# myapp/management/commands/start_celery.py

from django.core.management.base import BaseCommand
import subprocess
from threading import Thread

class Command(BaseCommand):
    help = 'Starts Celery worker and beat processes alongside the development server'
    print("Starts Celery worker and beat processes alongside the development server")
    def handle(self, *args, **options):
        worker_command = 'celery -A water_tank_system worker --loglevel=info'
        beat_command = 'celery -A water_tank_system beat -l info'

        worker_thread = Thread(target=subprocess.Popen, args=(worker_command,), kwargs={'shell': True})
        beat_thread = Thread(target=subprocess.Popen, args=(beat_command,), kwargs={'shell': True})

        worker_thread.start()
        beat_thread.start()

        # Run the development server
        self.stdout.write(self.style.SUCCESS('Starting Django development server...'))
        self.stdout.flush()
        self.run_server()

    def run_server(self):
        from django.core.management.commands.runserver import Command as RunServerCommand
        runserver_command = RunServerCommand()
        runserver_command.run(addrport=self.addrport)

