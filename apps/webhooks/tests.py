from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from apps.webhooks.models import WebhookPayload


class WebhookPayloadTestCase(TestCase):
    def setUp(self):
        self.webhook_receiver_url = reverse("api:webhook-receive")

    def test_webhook_payload_success(self):
        client = APIClient()
        payload = {"test": "test"}
        response = client.post(self.webhook_receiver_url, payload, format="json")

        self.assertEqual(response.status_code, 200)

    def test_webhook_payload_created(self):
        client = APIClient()
        payload = {"test": "test"}
        response = client.post(self.webhook_receiver_url, payload, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(WebhookPayload.objects.count(), 1)

    def test_webhook_payload_processed(self):
        client = APIClient()
        payload = {"test": "test"}
        response = client.post(self.webhook_receiver_url, payload, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(WebhookPayload.objects.count(), 1)

        # TODO: Figure out how to test that the task was processed
        # self.assertTrue(WebhookPayload.objects.first().success, "Webhook payload was not processed")
