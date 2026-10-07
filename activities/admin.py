from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    list_display = (
        "subject",
        "activity_type",
        "customer",
        "user",
        "activity_date",
    )

    search_fields = (
        "subject",
        "description",
    )

    list_filter = (
        "activity_type",
        "activity_date",
    )