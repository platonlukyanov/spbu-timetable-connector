import datetime
from dataclasses import dataclass
import os.path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from structures import ScheduleItem

# If modifying these scopes, delete the file token.json.
SCOPES = [
    # Allows for read, write, and delete access to the calendar events
    "https://www.googleapis.com/auth/calendar.events",
]

def setup_creds():
    """Template function from Google Calendar API documentation to get credentials"""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

@dataclass
class EventOptions:
    color_id: str = "3"

def create_event_info_from_schedule_item(schedule_item: ScheduleItem, options: EventOptions = EventOptions()):
    """Converts ScheduleItem to Google Calendar API event info dictionary, needed for creating an event"""
    day = schedule_item.day
    start = datetime.datetime.combine(day, schedule_item.start_time)
    end = datetime.datetime.combine(day, schedule_item.end_time)
    place = schedule_item.place
    subject = schedule_item.subject
    lecturer = schedule_item.lecturer

    return {
        "summary": subject,
        "start": {
            "dateTime": start.isoformat(),
            "timeZone": "Europe/Moscow",
        },
        "end": {
            "dateTime": end.isoformat(),
            "timeZone": "Europe/Moscow",
        },
        "location": place,
        "description": f"Преподаватель: {lecturer}",
        "colorId": options.color_id,
    }

def create_event(service, schedule_item: ScheduleItem, calendar_id: str, options: EventOptions = EventOptions()):
    """Creates a new event in Google Calendar API from ScheduleItem in the specified calendar"""
    event_info = create_event_info_from_schedule_item(schedule_item, options)
    try:
        service.events().insert(
            calendarId=calendar_id,
            body=event_info,
        ).execute()
    except HttpError as e:
        print(f"An error occurred: {e}")

def get_service():
    """Shorthand for getting Google Calendar API service"""
    creds = setup_creds()
    return build("calendar", "v3", credentials=creds)

def main():
    service = get_service()
    print('SUCCESS GETTING SERVICE')