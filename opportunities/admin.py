from django.contrib import admin
from .models import Opportunity


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "customer",
        "amount",
        "probability",
        "stage",
        "expected_close_date",
        "owner",
        "created_at",
    )

    search_fields = (
        "name",
        "customer__name",
    )

    list_filter = (
        "stage",
        "expected_close_date",
        "created_at",
    )