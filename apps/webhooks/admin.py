from django.contrib import admin

from .models import WebhookPayload


@admin.register(WebhookPayload)
class WebhookPayloadAdmin(admin.ModelAdmin):
    list_display = ("payload", "success", "created_at")
    list_filter = ("success", "created_at")
    search_fields = ("payload",)
