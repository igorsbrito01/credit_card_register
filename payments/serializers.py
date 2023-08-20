from rest_framework import serializers

from .models import CreditCard
from .utils import create_formated_date_with_day


class CreditCardCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ("id", "holder", "number", "brand")


class CreditCardCreateSerializer(serializers.ModelSerializer):
    exp_date = serializers.CharField(max_length=7)
    cvv = serializers.CharField(max_length=4, required=False)

    class Meta:
        model = CreditCard
        fields = ("id", "holder", "number", "cvv", "exp_date")

    # TODO: Validate data
    # TODO: encript number

    def create(self, validated_data):
        if "cvv" in validated_data:
            cvv_str = validated_data.pop("cvv")
            validated_data["cvv"] = int(cvv_str)

        exp_date_str = validated_data.pop("exp_date")
        exp_date = create_formated_date_with_day(exp_date_str)
        validated_data["exp_date"] = exp_date

        return super().create(validated_data)
