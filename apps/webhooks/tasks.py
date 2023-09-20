from celery import shared_task

from .models import WebhookPayload


@shared_task
def process_webhook_event(payload):
    try:
        payload_instance = WebhookPayload.objects.get(payload=payload)
        payload_instance.success = True
        payload_instance.save()
    except WebhookPayload.DoesNotExist:
        pass
