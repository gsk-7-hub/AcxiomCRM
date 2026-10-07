from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from leads.models import Lead


class Opportunity(models.Model):

    STAGE_CHOICES = [
        ("Prospecting", "Prospecting"),
        ("Qualification", "Qualification"),
        ("Proposal", "Proposal"),
        ("Negotiation", "Negotiation"),
        ("Won", "Won"),
        ("Lost", "Lost"),
    ]

    name = models.CharField(max_length=150)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="opportunities"
    )

    lead = models.ForeignKey(
        Lead,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="opportunities"
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="opportunities"
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    probability = models.PositiveIntegerField(
        default=50
    )

    stage = models.CharField(
        max_length=30,
        choices=STAGE_CHOICES,
        default="Prospecting"
    )

    expected_close_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name