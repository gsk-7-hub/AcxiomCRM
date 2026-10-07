from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        "action",
        "user",
        "model_name",
        "object_id",
        "ip_address",
        "timestamp",
    )

    search_fields = (
        "description",
        "model_name",
        "object_id",
        "ip_address",
    )

    list_filter = (
        "action",
        "timestamp",
    )

    readonly_fields = (
        "user",
        "action",
        "model_name",
        "object_id",
        "description",
        "ip_address",
        "timestamp",
    )