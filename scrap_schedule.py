from typing import Iterable
import openpyxl
from io import BytesIO
from _http import get_file_bytes_by_url
from __csv import convert_schedule_to_csv
from structures import ScheduleItem
from dateformat_utils import convert_russian_day_to_datetime_day, convert_hhmm_to_time
from timetable_spbu import get_file_download_url_from_timetable_spbu, setup_russian_timetable_spbu_session
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

def get_the_sheet(student_group_id: int, week_monday: str):
    """Gets the excel sheet of a timetable from the web"""
    session = setup_russian_timetable_spbu_session()
    url = get_file_download_url_from_timetable_spbu(student_group_id, week_monday)
    bytes = get_file_bytes_by_url(url, session)

    workbook = openpyxl.load_workbook(BytesIO(bytes))
    return workbook['Расписание студенческой группы']

def get_raw_schedule(sheet):
    """Selects rows from sheet correctly to get raw schedule"""
    schedule = []

    for row in sheet.iter_rows(min_row=5, max_row=300, max_col=5):
        schedule.append([cell.value.replace('\n', ' ') if cell.value is not None else cell.value for cell in row])

    # Remove empty rows
    schedule = [row for row in schedule if any(row)]

    # Replace None values in first column with previos values in the same column
    for row_index in range(len(schedule)):
        if schedule[row_index][0] is None:
            schedule[row_index][0] = schedule[row_index - 1][0]

    return schedule

def clean_schedule(schedule: Iterable[Iterable[str]]):
    """Converts 'list of lists' schedule to a list of strucutured ScheduleItem's"""
    cleaned_schedule = []

    for row in schedule:
        day = convert_russian_day_to_datetime_day(row[0].split()[1] + ' ' + row[0].split()[2])
        start_time = convert_hhmm_to_time(row[1].split('–')[0])
        end_time = convert_hhmm_to_time(row[1].split('–')[1])

        subject = row[2]
        lecturer = row[4]
        place = row[3]

        cleaned_schedule.append(ScheduleItem(day, start_time, end_time, subject, lecturer, place))

    return cleaned_schedule

def scrap_schedule(student_group_id: int = 411662, week_monday: str = '2024-09-02'):
    """Gets all the available schedule from the web and returns it correctly"""
    start_date = week_monday

    schedule = []
    last_schedule = True

    while last_schedule:
        sheet = get_the_sheet(student_group_id, start_date)
        last_schedule = clean_schedule(get_raw_schedule(sheet))

        if not last_schedule:
            break
        schedule += last_schedule
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d') + datetime.timedelta(days=7)
        start_date = start_date.strftime('%Y-%m-%d')

    return schedule

def main():
    start_date = os.environ['START_DATE']

    schedule = scrap_schedule(os.environ['GROUP_ID'], start_date)
    convert_schedule_to_csv(schedule, 'schedule.csv')

if __name__ == '__main__':
    main()