def is_armstrong(number):
    number_str = str(number)
    armstrong_sum = 0
    exponent = len(number_str)
    for number_char in number_str:
        armstrong_sum += int(number_char) ** exponent

    return armstrong_sum == number
