from datetime import datetime, date
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def get_days_from_today(target_date):
    today = date.today()
    delta_days = (target_date - today).days
    return delta_days