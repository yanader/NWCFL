from datetime import datetime as dt
from datetime import timedelta


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_date():
    day_offset = 1   # I can use this to test for a different date
    time_delta = timedelta(days=day_offset)
    today = dt.now()
    return_day = today + time_delta
    return return_day.strftime('%A {S} %B %Y').replace('{S}', str(return_day.day) + suffix(return_day.day))
