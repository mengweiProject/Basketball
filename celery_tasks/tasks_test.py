import time
from celery_tasks import app

@app.task
def add(x, y):
    time.sleep(1)
    return x + y