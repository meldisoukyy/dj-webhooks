from celery import shared_task


@shared_task
def webhook_task(*args, **kwargs):
    # do something
    pass
