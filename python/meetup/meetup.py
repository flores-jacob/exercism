from datetime import date
import calendar

def meetup_day(year, month, day_of_the_week, which):

    if which == "teenth":
        for day in range(13, 20):
            teenth_date = date(year, month, day)
            if calendar.day_name[teenth_date.weekday()] == day_of_the_week:
                return teenth_date

    if which == "1st":
        count_req = 1
    elif which == "2nd":
        count_req = 2
    elif which == "3rd":
        count_req = 3
    elif which == "4th":
        count_req = 4
    elif which == "5th":
        count_req = 5
    elif which == "last":
        count_req = -1
    else:
        raise ("Invalid input")

    day_count = 0
    if 1 <= count_req <=5:
        for day in range(1, 31):
            desired_date = date(year, month, day)
            if calendar.day_name[desired_date.weekday()] == day_of_the_week:
                day_count += 1
                if day_count == count_req:
                    return desired_date
    elif count_req == -1:
        last_day_of_month = calendar.monthrange(year, month)[1]
        for day in range(last_day_of_month, 1, -1):
            desired_date = date(year, month, day)
            if calendar.day_name[desired_date.weekday()] == day_of_the_week:
                return desired_date