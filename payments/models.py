from django.db import models


class CreditCard(models.Model):
    holder = models.CharField(max_length=255, null=False, blank=False)
    number = models.TextField(null=False, blank=False)
    cvv = models.CharField(max_length=4, blank=True)
    exp_date = models.DateField(null=False, blank=False)
    brand = models.CharField(max_length=500, null=False, blank=False)

    def __repr__(self) -> str:
        return f"Credit Card - {self.holder} - {self.number[-4:]}"
