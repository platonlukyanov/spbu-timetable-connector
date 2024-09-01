
from __csv import read_all_subjects_and_color_ids_from_csv
from _google import EventOptions, get_service, create_event
from scrap_schedule import scrap_schedule
import os
from dotenv import load_dotenv
load_dotenv()

CALENDAR_ID = os.environ['GOOGLE_CALENDAR_ID']
START_DATE = os.environ['START_DATE']
GROUP_ID = os.environ['GROUP_ID']

def main():
    service = get_service()
    subjects_and_colors = read_all_subjects_and_color_ids_from_csv('subjects.csv')
    schedule = scrap_schedule(GROUP_ID, START_DATE)

    for item in schedule:
        create_event(service, item, CALENDAR_ID, options=EventOptions(color_id=subjects_and_colors[item.subject].strip()))

if __name__ == '__main__':
    main()