# alx_travel_app/celery.py
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alx_travel_app.settings")

# Create Celery app instance
app = Celery("alx_travel_app")

# Load task modules from all registered Django apps.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Optional: simple debug log to check if Celery is running
@app.task(bind=True)
def debug_task(self):
    print(f"Celery task running: {self.request!r}")
