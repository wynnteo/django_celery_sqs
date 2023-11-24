import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = Celery("backend")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# simple task to print all the metadata
@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))