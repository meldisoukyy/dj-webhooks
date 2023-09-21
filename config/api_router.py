from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.users.api.views import UserViewSet
from apps.webhooks.api.views import WebhookReceiverAPIView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("webhooks/receive/", WebhookReceiverAPIView.as_view(), name="webhook-receive"),
]
