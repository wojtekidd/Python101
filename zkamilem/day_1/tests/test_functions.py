import pytest

from day_1.functions import format_phone_number
from day_1.functions import less_than
from day_1.functions import remove_duplicates
from day_1.functions import is_palindrom
from day_1.functions import safe_division


#@pytest.mark.skip
def test_format_number():
    assert format_phone_number('697120906') == '+48 (0) 697-120-906'
    assert format_phone_number('697120906', area_code='+10') == '+10 (0) 697-120-906'
    assert format_phone_number('697120906', delimeter='+') == '+48 (0) 697+120+906'
    assert format_phone_number('697120906', '+48', '+') == '+48 (0) 697+120+906'
    data = {
        'number': '697120906',
        'area_code': '+48',
        'delimeter': '+'
    }
    data_list = ['697120906', '+48', '+']
    assert format_phone_number(**data) == '+48 (0) 697+120+906'
    assert format_phone_number(*data_list) == '+48 (0) 697+120+906'


@pytest.mark.skip
@pytest.mark.parametrize("test_input,expected", [
    ('697120906', '+48 (0) 697-120-906'),
    # TODO #2 zmodyfikuj test i test_input tak aby można było przekazać też opcjonalne argumenty
])
def test_format_number_advanced(test_input, expected):
    assert format_phone_number(test_input) == expected


@pytest.mark.skip
def test_less_than():
    # TODO #3 popraw test ;)
    data = {
        'cutoff_val': 5,
        'values': [1, 2, 8]
    }
    assert less_than(**data) == [1, 2]


@pytest.mark.skip
@pytest.mark.parametrize("test_input,expected", [
    ('ala', True),
    ('igor łamał rogi', True),
    ('Ala ma kota', False),
])
def test_is_palindrom(test_input, expected):
    # TODO #4 popraw funkcje tak aby test przeszedł
    assert is_palindrom(test_input) == expected


@pytest.mark.skip
def test_remove_duplicates():
    # TODO #5 popraw test i funkcje
    list_without_duplicates = remove_duplicates(['Jan', 'Magda', 'Monika'])
    assert list_without_duplicates == (['Jan', 'Magda', 'Monika'], True)


@pytest.mark.skip
def test_safe_division():
    # TODO #6 popraw funkcje tak aby test przeszedł, dodaj kolejne testy
    assert safe_division(10, 2) == 5.0
    with pytest.raises(ZeroDivisionError):
        safe_division(10, 0)
