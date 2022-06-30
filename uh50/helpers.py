""" helper functions """
from dateutil import parser


def is_date(string):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    """
    try:
        parser.parse(string)
        return True

    except ValueError:
        return False


def is_float(string):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    """
    if "." not in string:
        return False

    if string.replace(".", "", 1).isdigit():
        return True

    return False
