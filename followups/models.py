from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from leads.models import Lead
from opportunities.models import Opportunity


class FollowUp(models.Model):

    TYPE_CHOICES = [
        ("Call", "Call"),
        ("Meeting", "Meeting"),
        ("Email", "Email"),
        ("Task", "Task"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    opportunity = models.ForeignKey(
        Opportunity,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )

    followup_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default="Call"
    )

    subject = models.CharField(max_length=200)

    due_date = models.DateTimeField()

    completed = models.BooleanField(default=False)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject