import calendar
from datetime import datetime
from cryptography.fernet import Fernet

from django.conf import settings


def create_formated_date_with_day(exp_date: str) -> str:
    month = int(exp_date.split("/")[0])
    year = int(exp_date.split("/")[1])

    _, last_day = calendar.monthrange(year, month)
    date = datetime.strptime(f"{last_day}/{month}/{year}", "%d/%m/%Y").date()

    return date.strftime("%Y-%m-%d")


def encrypt(value: str) -> str:
    fernet = Fernet(settings.CRYPTOGRAPHY_KEY.encode())
    encrypted_bytes = fernet.encrypt(value.encode())

    return encrypted_bytes.decode()


def decrypt(encrypted_value: str) -> str:
    fernet = Fernet(settings.CRYPTOGRAPHY_KEY.encode())
    decrypted_value_bytes = fernet.decrypt(encrypted_value.encode())

    return decrypted_value_bytes.decode()


def hide_cc_numbers(number: str) -> str:
    ending = number[-3:]
    hide_part = number[:-3]

    hide_str = "".join(["*" for iten in hide_part])

    return hide_str + ending
