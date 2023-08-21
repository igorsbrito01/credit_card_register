from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.test import TestCase

from payments.serializers import CreditCardCreateSerializer


class CreditCardCreateSerializerTest(TestCase):
    """
    Test the validation when uses the serializer to create credit cards
    """

    def test_valid_data(self):
        date = datetime.now() + relativedelta(months=1)
        data = {
            "id": 1,
            "holder": "Igor",
            "number": "4539578763621486",
            "cvv": "344",
            "exp_date": date.strftime("%m/%Y"),
        }
        serializer = CreditCardCreateSerializer(data=data)
        self.assertEqual(serializer.is_valid(), True)

    def test_wrong_format_expiration_date(self):
        """
        Test the format of the value at the expiration date field
        """
        data = {
            "id": 1,
            "holder": "Igor",
            "number": "4539578763621486",
            "cvv": "344",
            "exp_date": "022022",
        }
        serializer = CreditCardCreateSerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(list(serializer.errors.keys()), ["exp_date"])
        self.assertEqual(
            list(serializer.errors.values())[0],
            ["Expiration date is not in the proper format"],
        )

    def test_past_date_expiration_date(self):
        """
        Test the passing a old date at the expiration date field
        """
        old_date = datetime.now() - relativedelta(months=1)

        data = {
            "id": 1,
            "holder": "Igor",
            "number": "4539578763621486",
            "cvv": "344",
            "exp_date": old_date.strftime("%m/%Y"),
        }
        serializer = CreditCardCreateSerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(list(serializer.errors.keys()), ["exp_date"])
        self.assertEqual(
            list(serializer.errors.values())[0],
            ["Expiration date is a past date"],
        )

    def test_invalid_holder(self):
        date = datetime.now() + relativedelta(months=1)
        data = {
            "id": 1,
            "holder": "Ig",
            "number": "4539578763621486",
            "cvv": "344",
            "exp_date": date.strftime("%m/%Y"),
        }
        serializer = CreditCardCreateSerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(list(serializer.errors.keys()), ["holder"])
        self.assertEqual(
            list(serializer.errors.values())[0],
            ["Ensure this field has at least 3 characters."],
        )

    def test_invalid_number(self):
        date = datetime.now() + relativedelta(months=1)
        data = {
            "id": 1,
            "holder": "Igor",
            "number": "000000001",
            "cvv": "344",
            "exp_date": date.strftime("%m/%Y"),
        }
        serializer = CreditCardCreateSerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(list(serializer.errors.keys()), ["number"])
        self.assertEqual(
            list(serializer.errors.values())[0],
            ["Card number is invalid"],
        )

    def test_invalid_cvv(self):
        date = datetime.now() + relativedelta(months=1)
        data = {
            "id": 1,
            "holder": "Igor",
            "number": "4539578763621486",
            "cvv": "34",
            "exp_date": date.strftime("%m/%Y"),
        }
        serializer = CreditCardCreateSerializer(data=data)
        self.assertEqual(serializer.is_valid(), False)
        self.assertEqual(list(serializer.errors.keys()), ["cvv"])
        self.assertEqual(
            list(serializer.errors.values())[0],
            ["Ensure this field has at least 3 characters."],
        )
