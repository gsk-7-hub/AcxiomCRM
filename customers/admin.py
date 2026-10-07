from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "company",
        "status",
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
        "created_at",
    )