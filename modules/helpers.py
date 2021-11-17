import datetime
from modules.CONST import Const

def convert_without_time(date):
    if isinstance(date, datetime.date):
        date = date.strftime('%d.%m.%Y')
        return date
    else:
        return 'Время не является экземпляром класса datetime'

def convert_with_time(date):
    if isinstance(date, datetime.date):
        date = date.strftime('%Y-%m-%dT%H:%M:%S+03:00')
        return date
    else:
        return 'Время не является экземпляром класса datetime'
