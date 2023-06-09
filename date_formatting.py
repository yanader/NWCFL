from datetime import datetime as dt
from datetime import timedelta


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_date(*args):
    day_offset = 0
    if len(args) == 1:
        day_offset += args[0]

    time_delta = timedelta(days=day_offset)
    today = dt.now()
    return_day = today + time_delta
    return return_day.strftime('%A {S} %B %Y').replace('{S}', str(return_day.day) + suffix(return_day.day))

