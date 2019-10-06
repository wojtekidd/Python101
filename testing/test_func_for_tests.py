import func_for_tests


def test_add():

    assert func_for_tests.add(7, 3) == 10
    assert func_for_tests.add(2, 4) == 6
    assert func_for_tests.add(4.3, 5.3) == 9.6


def test_multiply():

    assert func_for_tests.multiply(7, 3) == 21
    assert func_for_tests.multiply(2, 4) == 8
    assert func_for_tests.multiply(4.3, 5.3) == 22.79


def test_invert_str():

    assert func_for_tests.invert_str("1234") == "4321"
    assert func_for_tests.invert_str("Wojtek") == "ketjoW"


def test_is_palindrom():

    assert func_for_tests.is_palindrom("1221") is True
    assert func_for_tests.is_palindrom("abba") is True
    assert func_for_tests.is_palindrom("asdf") is False


test_add()
test_multiply()
test_invert_str()
test_is_palindrom()
