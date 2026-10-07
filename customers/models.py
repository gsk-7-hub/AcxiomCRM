from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    name = models.CharField(max_length=150)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    company = models.CharField(
        max_length=150,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="customers"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
