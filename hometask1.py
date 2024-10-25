from datetime import datetime, date
def string_to_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y.%m.%d").date()
    except ValueError:
        raise ValueError("Використовуйте формат YYYY.MM.DD")

def get_days_from_today(target_date):
    target_date = string_to_date(target_date)
    today = date.today()
    delta_days = (target_date - today).days
    return delta_days