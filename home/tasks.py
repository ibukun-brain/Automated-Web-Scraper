import time
from celery import Celery, shared_task

app = Celery()

# allows you to call this function asynchronously
@shared_task
def send_mass_emails(recipent):
    print(recipent)
    print("Started to sleep")
    time.sleep(5)
    print("Work up from sleep")
    return recipent

@app.task
def send_schedule_emails():
    # fetch all those email addresses
    pass

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'tasks.send_schedule_emails',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }