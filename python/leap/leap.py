def is_leap_year(year):
    # if the year is divisible by 4 AND if it's either not divisible by 100 or divisible by 400,
    # then it's a leap year
    return (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0))

