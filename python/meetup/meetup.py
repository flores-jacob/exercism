from datetime import date
import calendar

def meetup_day(year, month, day_of_the_week, which):

    for day in range(13, 20):
        teenth_date = date(year, month, day)
        if calendar.day_name[teenth_date.weekday()] == day_of_the_week:
            return teenth_date