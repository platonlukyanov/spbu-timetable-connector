import datetime

def convert_russian_day_to_datetime_day(russian_name_day: str, year: int = 2024) -> datetime.date:
    """Converts format like '3 сентября' to actual datetime.date"""
    months = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12
    }

    day, month = russian_name_day.split()

    return datetime.date(year, months[month], int(day))

def convert_hhmm_to_time(hhmm: str):
    hours, minutes = hhmm.split(':')
    return datetime.time(hour=int(hours), minute=int(minutes))
