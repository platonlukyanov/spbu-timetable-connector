from typing import Iterable
from structures import ScheduleItem
from utils import assign_numbers_to_each_string

def convert_schedule_to_csv(schedule: Iterable[ScheduleItem], filename: str):
    """
    Convert a schedule of items into a CSV file.
    Args:
        schedule (Iterable[ScheduleItem]): The schedule to convert.
        filename (str): The name of the CSV file to create.
    """
    csv = 'day;start_time;end_time;subject;lecturer;place\n'
    for item in schedule:
        csv += f'{item.day.isoformat()};{item.start_time.isoformat()};{item.end_time.isoformat()};{item.subject};{item.lecturer};{item.place}\n'
    
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(csv)

def get_all_unique_subjects_from_csv(filename: str):
    """
    Retrieves all unique subjects from a CSV file.
    Args:
        filename (str): The path to the CSV file.
    Returns:
        set: A set containing all unique subjects found in the CSV file.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    subjects = set()
    for line in lines[1:]:
        subject = line.split(';')[3]
        subjects.add(subject)
    
    return subjects

def assign_all_unique_subjects_to_colors(filename: str):
    """Each subject is assigned a unique color id from 1 to 11"""
    unique_subjects = get_all_unique_subjects_from_csv(filename)
    assigned = assign_numbers_to_each_string(unique_subjects, list(range(1, 12)))

    return assigned
    
def dump_assigned_subjects_to_csv(assigned: dict, filename: str = 'subjects.csv'):
    """Dump assigned subjects to a CSV file"""
    unique_subjects = list(assigned.keys())
    with open(filename, 'w', encoding="utf-8") as file:
        for subject in unique_subjects:
            file.write(f'{subject};{assigned[subject]}\n')

def read_all_subjects_and_color_ids_from_csv(filename: str = 'subjects.csv'):
    """Create a structure from a CSV file where the key is the subject and the value is the color id"""
    dictionary = {}

    with open(filename, 'r', encoding="utf-8") as file:
        for line in file.readlines():
            subject, color_id = line.split(';')
            dictionary[subject] = color_id
        
    return dictionary

def main():
    assigned = assign_all_unique_subjects_to_colors('schedule.csv')
    dump_assigned_subjects_to_csv(assigned)
    

if __name__ == '__main__':
    main()
