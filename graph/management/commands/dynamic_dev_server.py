import time

from subprocess import call

from django.core.management.base import BaseCommand, CommandError

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChecker(FileSystemEventHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_change = 0

    def on_created(self, event):
        if time.time() - self.last_change > 1:
            self.changes(event)
            self.last_change = time.time()

    def on_modified(self, event):
        if time.time() - self.last_change > 1:
            self.changes(event)
            self.last_change = time.time()

    def changes(self, event):
        print("A change was detected on the static files folder")
        print("Compiling scss files")
        call("npm run sass", shell=True)
        print("Linting js files")
        call("npm run lint", shell=True)

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass
        #parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        event_handler = FileChecker()
        observer = Observer()
        observer.schedule(event_handler, path="static", recursive=True)
        observer.start()
        call("python manage.py runserver", shell=True)

