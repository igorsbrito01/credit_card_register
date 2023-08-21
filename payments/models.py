from django.db import models
from django.core.validators import MaxValueValidator

from .utils import get_brand_from_cc_number, encrypt


class CreditCard(models.Model):
    holder = models.CharField(max_length=255, null=False, blank=False)
    number = models.TextField(null=False, blank=False)
    cvv = models.IntegerField(validators=[MaxValueValidator(4)], blank=True, null=True)
    exp_date = models.CharField(max_length=10, null=False, blank=False)
    brand = models.CharField(max_length=500, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self) -> str:
        return f"Credit Card - {self.holder} - {self.number}"

    def save(self, *args, **kwargs):
        # The encryptation should be inside the save,
        # to avoid mistakes from the developer when use this model
        self.brand = get_brand_from_cc_number(self.number)
        self.number = encrypt(self.number)

        super().save(*args, **kwargs)
