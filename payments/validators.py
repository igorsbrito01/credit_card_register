from creditcard import CreditCard
from creditcard.exceptions import BrandNotFound
from datetime import datetime

from django.core.exceptions import ValidationError

from .utils import create_formated_date_with_day


def validate_expiration_date_str(exp_date):
    try:
        _ = datetime.strptime(exp_date, "%m/%Y")
    except ValueError:
        raise ValidationError("Expiration date is not in the proper format")

    date_str = create_formated_date_with_day(exp_date)
    card_date = datetime.strptime(date_str, "%Y-%m-%d").date()

    now = datetime.now().date()
    if card_date < now:
        raise ValidationError("Expiration date is a past date")


def validate_credit_card_number(card_number):
    cc = CreditCard(card_number)
    if not cc.is_valid():
        raise ValidationError("Card number is invalid")

    try:
        cc.get_brand()
    except BrandNotFound:
        raise ValidationError("Card number brand not found")
