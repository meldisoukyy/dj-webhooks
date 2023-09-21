from rest_framework import status, views
from rest_framework.response import Response

from apps.webhooks.models import WebhookPayload
from apps.webhooks.tasks import webhook_task


class WebhookReceiverAPIView(views.APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        payload = request.data
        WebhookPayload.objects.create(payload=payload)

        webhook_task.delay()

        return Response(status=status.HTTP_200_OK, data={"message": "Webhook payload received"})
