from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer


class Lead(models.Model):

    STATUS_CHOICES = [
        ("New", "New"),
        ("Contacted", "Contacted"),
        ("Qualified", "Qualified"),
        ("Converted", "Converted"),
        ("Lost", "Lost"),
    ]

    SOURCE_CHOICES = [
        ("Website", "Website"),
        ("Referral", "Referral"),
        ("Email", "Email"),
        ("Phone", "Phone"),
        ("Social Media", "Social Media"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    company = models.CharField(
        max_length=150,
        blank=True
    )

    source = models.CharField(
        max_length=30,
        choices=SOURCE_CHOICES,
        default="Website"
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="New"
    )

    estimated_value = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads"
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leads"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name