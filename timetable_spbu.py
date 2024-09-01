
import requests

def get_file_download_url_from_timetable_spbu(student_group_id: int, week_monday: str):
    return f'https://timetable.spbu.ru/StudentGroupEvents/ExcelWeek?studentGroupId={student_group_id}&weekMonday={week_monday}'

def setup_russian_timetable_spbu_session():
    """timetable.spbu.ru requires cookies to get russian language sheets, otherwise it is delivered in english"""
    session = requests.Session()
    # Set a cookie
    session.cookies.set('_culture', 'ru', domain='timetable.spbu.ru')
    return session
