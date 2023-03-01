from celery.schedules import crontab

CELERY_TIMEZONE = "Africa/Lagos"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BROKER_URL = 'redis://localhost:6379/'
CELERY_BEAT_SCHEDULE = {
    'SendScheduledEmails': {
        'task':'home.tasks.send_schedule_emails',
        'schedule':  crontab(minute="*/30") # every 30 minutes
    }
}
