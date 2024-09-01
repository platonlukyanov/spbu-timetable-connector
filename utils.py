from typing import Iterable

def zip_two_lists(list1: Iterable, list2: Iterable):
    """zips two lists, and if one of them is shorter, starts from the beginning"""
    if len(list1) > len(list2):
        return zip(list1, list2 * len(list1))
    elif len(list1) < len(list2):
        return zip(list1 * len(list2), list2)
    else:
        return zip(list1, list2)

def assign_numbers_to_each_string(strings: Iterable[str], numbers_available: Iterable[str]) -> dict:
    """Loops through given numbers and assigns them to strings in a dictionary format"""
    zipped = zip_two_lists(numbers_available, strings)
    return {string: i for i, string in zipped}
