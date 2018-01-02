from datetime import date
import calendar


def meetup_day(year, month, day_of_the_week, which):

    if which == "teenth":
        date_range = range(13, 20)
    elif which == "last":
        last_day_of_month = calendar.monthrange(year, month)[1]
        date_range = range(last_day_of_month, 1, -1)
    else:
        date_range = range(1, 31)

    count_req_dict = {"1st": 1, "2nd": 2, "3rd": 3, "4th": 4, "5th": 5, "last": 1, "teenth": 1}

    day_count = 0
    count_req = count_req_dict[which]
    for day in date_range:
        desired_date = date(year, month, day)
        if calendar.day_name[desired_date.weekday()] == day_of_the_week:
            day_count += 1
            if day_count == count_req:
                return desired_date
