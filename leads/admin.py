from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "company",
        "status",
        "source",
        "estimated_value",
        "owner",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "company",
    )

    list_filter = (
        "status",
        "source",
        "created_at",
    )