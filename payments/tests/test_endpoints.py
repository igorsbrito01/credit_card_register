from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from payments.models import CreditCard


class CreditCardViewTest(TestCase):
    def setUp(self) -> None:
        self.auth_client = APIClient()
        self.user = User.objects.create(
            username="test_user", password="123456", email="test@dev.com"
        )
        self.auth_client.force_authenticate(user=self.user)
        return super().setUp()

    def test_create_credit_card(self):
        date = datetime.now() + relativedelta(months=1)
        payload = {
            "holder": "user development",
            "number": "4539578763621486",
            "cvv": "345",
            "exp_date": date.strftime("%m/%Y"),
        }
        response = self.auth_client.post(reverse("payments:creditcard"), payload)

        self.assertEqual(response.status_code, 201)

        cc = CreditCard.objects.get(holder="user development")

        self.assertEqual(cc.cvv, 345)
        self.assertEqual(cc.brand, "visa")

    def test_list_credit_cards(self):
        date = datetime.now() + relativedelta(months=1)
        payload = {
            "holder": "user development",
            "number": "4539578763621486",
            "cvv": "345",
            "exp_date": date.strftime("%m/%Y"),
        }
        response = self.auth_client.post(reverse("payments:creditcard"), payload)

        self.assertEqual(response.status_code, 201)
        response = self.auth_client.get(reverse("payments:creditcard"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["holder"], "user development")

    def test_credit_cards_by_id(self):
        date = datetime.now() + relativedelta(months=1)
        payload = {
            "holder": "user development",
            "number": "4539578763621486",
            "cvv": "345",
            "exp_date": date.strftime("%m/%Y"),
        }
        response = self.auth_client.post(reverse("payments:creditcard"), payload)

        self.assertEqual(response.status_code, 201)
        cc = CreditCard.objects.get(holder="user development")

        response = self.auth_client.get(reverse("payments:creditcardpk", args=[cc.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["holder"], "user development")

    def test_create_credit_card_wrong_format_expiration_date(self):
        payload = {
            "holder": "user development",
            "number": "4539578763621486",
            "cvv": "345",
            "exp_date": "022027",
        }
        response = self.auth_client.post(reverse("payments:creditcard"), payload)

        self.assertEqual(response.status_code, 400)

        self.assertEqual(list(response.data.keys()), ["exp_date"])
        self.assertEqual(
            list(response.data.values())[0],
            ["Expiration date is not in the proper format"],
        )

    def test_create_credit_card_past_date_expiration_date(self):
        date = datetime.now() - relativedelta(months=1)
        payload = {
            "holder": "user development",
            "number": "4539578763621486",
            "cvv": "345",
            "exp_date": date.strftime("%m/%Y"),
        }
        response = self.auth_client.post(reverse("payments:creditcard"), payload)

        self.assertEqual(response.status_code, 400)

        self.assertEqual(list(response.data.keys()), ["exp_date"])
        self.assertEqual(
            list(response.data.values())[0],
            ["Expiration date is a past date"],
        )

    def test_create_credit_card_invalid_holder(self):
        date = datetime.now() + relativedelta(months=1)
        payload = {
            "holder": "us",
            "number": "4539578763621486",
            "cvv": "345",
            "exp_date": date.strftime("%m/%Y"),
        }
        response = self.auth_client.post(reverse("payments:creditcard"), payload)

        self.assertEqual(response.status_code, 400)

        self.assertEqual(list(response.data.keys()), ["holder"])
        self.assertEqual(
            list(response.data.values())[0],
            ["Ensure this field has at least 3 characters."],
        )

    def test_create_credit_card_invalid_number(self):
        date = datetime.now() + relativedelta(months=1)
        payload = {
            "holder": "user development",
            "number": "4539578763621486324",
            "cvv": "345",
            "exp_date": date.strftime("%m/%Y"),
        }
        response = self.auth_client.post(reverse("payments:creditcard"), payload)

        self.assertEqual(response.status_code, 400)

        self.assertEqual(list(response.data.keys()), ["number"])
        self.assertEqual(
            list(response.data.values())[0],
            ["Card number is invalid"],
        )

    def test_create_credit_card_invalid_cvv(self):
        date = datetime.now() + relativedelta(months=1)
        payload = {
            "holder": "user development",
            "number": "4539578763621486",
            "cvv": "34",
            "exp_date": date.strftime("%m/%Y"),
        }
        response = self.auth_client.post(reverse("payments:creditcard"), payload)

        self.assertEqual(response.status_code, 400)

        self.assertEqual(list(response.data.keys()), ["cvv"])
        self.assertEqual(
            list(response.data.values())[0],
            ["Ensure this field has at least 3 characters."],
        )

    def test_create_credit_card_all_wrong(self):
        date = datetime.now() - relativedelta(months=1)
        payload = {
            "holder": "us",
            "number": "45395787636214862313",
            "cvv": "34",
            "exp_date": date.strftime("%m/%Y"),
        }
        response = self.auth_client.post(reverse("payments:creditcard"), payload)

        self.assertEqual(response.status_code, 400)

        self.assertEqual(
            list(response.data.keys()), ["holder", "number", "cvv", "exp_date"]
        )
