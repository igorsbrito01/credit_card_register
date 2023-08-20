from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CreditCard(models.Model):
    holder = models.CharField(max_length=255, null=False, blank=False)
    number = models.TextField(null=False, blank=False)
    cvv = models.IntegerField(
        validators=[MaxValueValidator(4)],
        blank=True,
        null=True
    )
    exp_date = models.CharField(max_length=10, null=False, blank=False)
    brand = models.CharField(max_length=500, null=False, blank=False)

    def __repr__(self) -> str:
        return f"Credit Card - {self.holder} - {self.number}"
