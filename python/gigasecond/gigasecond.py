from datetime import timedelta


def add_gigasecond(birth_date):
    gigasecond = timedelta(seconds=1000000000)
    return birth_date + gigasecond
