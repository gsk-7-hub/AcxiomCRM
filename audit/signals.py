from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from customers.models import Customer
from leads.models import Lead
from opportunities.models import Opportunity

from .models import AuditLog


@receiver(post_save, sender=Customer)
def customer_saved(sender, instance, created, **kwargs):
    AuditLog.objects.create(
        user=instance.owner,
        action="CREATE" if created else "UPDATE",
        model_name="Customer",
        object_id=str(instance.id),
        description=f"Customer '{instance.name}' was {'created' if created else 'updated'}.",
    )


@receiver(post_delete, sender=Customer)
def customer_deleted(sender, instance, **kwargs):
    AuditLog.objects.create(
        action="DELETE",
        model_name="Customer",
        object_id=str(instance.id),
        description=f"Customer '{instance.name}' was deleted.",
    )


@receiver(post_save, sender=Lead)
def lead_saved(sender, instance, created, **kwargs):
    AuditLog.objects.create(
        user=instance.owner,
        action="CREATE" if created else "UPDATE",
        model_name="Lead",
        object_id=str(instance.id),
        description=f"Lead '{instance.name}' was {'created' if created else 'updated'}.",
    )


@receiver(post_delete, sender=Lead)
def lead_deleted(sender, instance, **kwargs):
    AuditLog.objects.create(
        action="DELETE",
        model_name="Lead",
        object_id=str(instance.id),
        description=f"Lead '{instance.name}' was deleted.",
    )


@receiver(post_save, sender=Opportunity)
def opportunity_saved(sender, instance, created, **kwargs):
    AuditLog.objects.create(
        user=instance.owner,
        action="CREATE" if created else "UPDATE",
        model_name="Opportunity",
        object_id=str(instance.id),
        description=f"Opportunity '{instance.name}' was {'created' if created else 'updated'}.",
    )


@receiver(post_delete, sender=Opportunity)
def opportunity_deleted(sender, instance, **kwargs):
    AuditLog.objects.create(
        action="DELETE",
        model_name="Opportunity",
        object_id=str(instance.id),
        description=f"Opportunity '{instance.name}' was deleted.",
    )