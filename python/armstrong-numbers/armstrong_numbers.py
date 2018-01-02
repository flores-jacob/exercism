def is_armstrong(number):
    number_str = str(number)
    armstrong_sum = 0
    for number_char in number_str:
        armstrong_sum += int(number_char) ** len(number_str)

    if armstrong_sum == number:
        return True
    else:
        return False
