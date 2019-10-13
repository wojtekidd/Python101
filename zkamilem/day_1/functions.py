from textwrap import wrap


def format_phone_number(number, area_code='+48', delimeter='-'):
    wrapped_number = delimeter.join(wrap(number, 3))
    return f"{area_code} (0) {wrapped_number}"
    pass


def less_than(cutoff_val, values):
    # funkcja powinna zwrócić wartości mniejsze od "cutoff_val" w liście "values"
    was_something_removed = False
    result = []
    for value in values:
        if value < cutoff_val:
            result.append(value)
        else:
            was_something_removed = True

    return result, was_something_removed




def is_palindrom(text):
    # funkcja powinna zwrócić wartość True jeśli zdanie jest palindrom i False jeśli nie.
    text = text.lower().strip().replace(',', ' ')
    return text == text[::-1]


def remove_duplicates(values):
    # funkcja powinna zwrócić listę bez duplikatów oraz informację czy był jakiś duplikat
    pass


def safe_division(number, divisor, ignore_zero_division):
    # funkcja na podstawie flagi ignore_zero_division powinno zwrócić float('inf') lub wyjątek
    # ignore_zero_division powinno domyślnie być False
    pass
