from datetime import datetime as dt

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_date():
    return dt.now().strftime('%A {S} %B %Y').replace('{S}', str(dt.now().day) + suffix(dt.now().day))