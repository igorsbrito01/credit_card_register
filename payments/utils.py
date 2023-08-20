import calendar
from datetime import datetime


def create_formated_date_with_day(exp_date: str) -> str:
    month = int(exp_date.split("/")[0])
    year = int(exp_date.split("/")[1])

    _, last_day = calendar.monthrange(year, month)
    date = datetime.strptime(f"{last_day}/{month}/{year}", "%d/%m/%Y").date()

    return date.strftime("%Y-%m-%d")
