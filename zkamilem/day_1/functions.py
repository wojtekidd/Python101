from textwrap import wrap
from typing import List
from typing import Tuple

def format_phone_number(number, area_code='+48', delimeter='-'):
    wrapped_number = delimeter.join(wrap(number, 3))
    return f"{area_code} (0) {wrapped_number}"
    pass


def less_than(cutoff_val: int, values: List[int]) -> Tuple[List[int], bool]:
    # funkcja powinna zwrócić wartości mniejsze od "cutoff_val" w liście "values"
    was_something_removed: bool = False
    result: List[int] = []
    for value in values:
        if value < cutoff_val:
            result.append(value)
        else:
            was_something_removed = True

    return result, was_something_removed




def is_palindrom(text):
    # funkcja powinna zwrócić wartość True jeśli zdanie jest palindrom i False jeśli nie.
    text = text.lower().replace(',', '').strip()
    return text == text[::-1]


def remove_duplicates(values):
    # funkcja powinna zwrócić listę bez duplikatów oraz informację czy był jakiś duplikat
    list1 = []
    was_a_duplicate = False
    for value in values:
        if value not in list1:
          list1.append(value)
        else:
            was_a_duplicate = True
    return sorted(list1), was_a_duplicate

# set_val = set(values)
# list_sorted = sorted(list(set_val))
# return list_sorted, was_a_duplicate



def safe_division(number: int, divisor: int, ignore_zero_division: bool=False) -> [int]:
    # funkcja na podstawie flagi ignore_zero_division powinno zwrócić float('inf') lub wyjątek
    # ignore_zero_division powinno domyślnie być False
    try:
        return number / divisor
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        raise
