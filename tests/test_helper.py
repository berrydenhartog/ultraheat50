from uh50.helpers import is_date, is_float


def test_is_float():
    assert is_float("123") is False
    assert is_float("123.2") is True
    assert is_float("12a3.2") is False


def test_is_date():
    assert is_date("2012-02-19") is True
    assert is_date("2012XXX") is False
