from rest_framework import serializers

from .models import CreditCard
from .utils import create_date_from_year_month


class CreditCardCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ("id", "holder", "number", "brand")


class CreditCardCreateCreateSerializer(serializers.ModelSerializer):
    exp_date = serializers.CharField(max_length=7)

    class Meta:
        model = CreditCard
        fields = ("id", "holder", "number", "cvv", "exp_date")

    # TODO: Validate data
    # TODO: encript number

    def create(self, validated_data):
        exp_date_str = validated_data.pop("exp_date")
        exp_date = create_date_from_year_month(
            int(exp_date_str.split("/")[0]), int(exp_date_str.split("/")[1])
        )
        validated_data["exp_date"] = exp_date

        return super().create(validated_data)
