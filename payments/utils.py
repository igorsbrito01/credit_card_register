import calendar
from datetime import datetime


def create_date_from_year_month(month, year):
    _, last_day = calendar.monthrange(year, month)
    return datetime.strptime(f"{last_day}/{month}/{year}", "%d/%m/%Y").date()
