from rest_framework import serializers

from .models import CreditCard
from .utils import create_formated_date_with_day
from .validators import validate_expiration_date_str, validate_credit_card_number


class CreditCardCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ("id", "holder", "number", "brand", "created_at", "updated_at")


class CreditCardCreateSerializer(serializers.ModelSerializer):
    exp_date = serializers.CharField(max_length=7)
    cvv = serializers.CharField(min_length=3, max_length=4, required=False)
    holder = serializers.CharField(min_length=3)

    class Meta:
        model = CreditCard
        fields = ("id", "holder", "number", "cvv", "exp_date")

    def validate_exp_date(self, value):
        validate_expiration_date_str(value)
        return value

    def validate_number(self, value):
        validate_credit_card_number(value)
        return value

    # TODO: encript number

    def create(self, validated_data):
        if "cvv" in validated_data:
            cvv_str = validated_data.pop("cvv")
            validated_data["cvv"] = int(cvv_str)

        exp_date_str = validated_data.pop("exp_date")
        exp_date = create_formated_date_with_day(exp_date_str)
        validated_data["exp_date"] = exp_date

        return super().create(validated_data)
