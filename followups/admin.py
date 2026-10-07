from django.contrib import admin
from .models import FollowUp


@admin.register(FollowUp)
class FollowUpAdmin(admin.ModelAdmin):

    list_display = (
        "subject",
        "followup_type",
        "customer",
        "lead",
        "opportunity",
        "assigned_to",
        "due_date",
        "completed",
    )

    search_fields = (
        "subject",
        "notes",
    )

    list_filter = (
        "followup_type",
        "completed",
        "due_date",
    )