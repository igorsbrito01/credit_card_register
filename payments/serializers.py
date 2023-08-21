from typing import Dict, Any

from rest_framework import serializers

from .models import CreditCard
from .utils import (
    create_formated_date_with_day,
    decrypt,
    hide_cc_numbers,
)
from .validators import validate_expiration_date_str, validate_credit_card_number


class CreditCardListSerializer(serializers.ModelSerializer):
    number = serializers.SerializerMethodField()

    class Meta:
        model = CreditCard
        fields = ("id", "holder", "number", "brand", "created_at", "updated_at")

    def get_number(self, obj: CreditCard) -> str:
        number = decrypt(obj.number)
        return hide_cc_numbers(number)


class CreditCardCreateSerializer(serializers.ModelSerializer):
    exp_date = serializers.CharField(max_length=7)
    cvv = serializers.CharField(min_length=3, max_length=4, required=False)
    holder = serializers.CharField(min_length=3)

    class Meta:
        model = CreditCard
        fields = ("id", "holder", "number", "cvv", "exp_date")

    def validate_exp_date(self, value: str) -> str:
        validate_expiration_date_str(value)
        return value

    def validate_number(self, value: str) -> str:
        validate_credit_card_number(value)
        return value

    def create(self, validated_data: Dict[str, Any]) -> CreditCard:
        if "cvv" in validated_data:
            cvv_str = validated_data.pop("cvv")
            validated_data["cvv"] = int(cvv_str)

        exp_date_str = validated_data.pop("exp_date")
        exp_date = create_formated_date_with_day(exp_date_str)
        validated_data["exp_date"] = exp_date

        return super().create(validated_data)
