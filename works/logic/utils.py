from datetime import datetime

DATE_FORMAT = "%d-%m-%Y"


def get_datetime_from_string(string: str, str_format: str = DATE_FORMAT):
    return datetime.strptime(string, str_format)
