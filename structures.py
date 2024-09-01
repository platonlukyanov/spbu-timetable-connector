from dataclasses import dataclass
import datetime

@dataclass
class ScheduleItem:
    day: datetime.date
    start_time: datetime.time
    end_time: datetime.time
    subject: str
    lecturer: str
    place: str
