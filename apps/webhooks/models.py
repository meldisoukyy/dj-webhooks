from django.db import models


class WebhookPayload(models.Model):
    payload = models.JSONField()
    success = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Webhook Payload"
        verbose_name_plural = "Webhook Payloads"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["created_at"]),
        ]
