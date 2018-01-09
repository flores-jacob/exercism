# python3
from collections import deque

def get_hundreds_text(number):
    if number <= 0:
        return "zero"

    ones_txt = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens_txt = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens_txt = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                 "nineteen"]

    # floor divide
    hundreds = number // 100
    tens_and_ones = number - (hundreds * 100)
    tens = tens_and_ones // 10
    ones = tens_and_ones - (tens * 10)

    if hundreds:
        hundreds_portion = " ".join([ones_txt[hundreds], "hundred"])
    else:
        hundreds_portion = ""

    if 10 <= tens_and_ones <= 19:
        tens_and_ones_portion = teens_txt[ones]
    else:
        tens_and_ones_portion = []
        if tens:
            tens_and_ones_portion.append(tens_txt[tens])
        if ones:
            tens_and_ones_portion.append(ones_txt[ones])
        tens_and_ones_portion = ("-".join(tens_and_ones_portion))

    if hundreds and tens_and_ones:
        in_words = " and ".join([hundreds_portion, tens_and_ones_portion])
    else:
        in_words = "".join([hundreds_portion, tens_and_ones_portion])

    return "".join(in_words)


def say(number):
    number_str = str(number)

    delimited_list = deque()
    build_str = ""
    count = 0
    for i in range(len(number_str) - 1, -1, -1):
        count += 1
        build_str = number_str[i] + build_str
        if (count == 3) or (i == 0):
            delimited_list.appendleft(build_str)
            count = 0
            build_str = ""

    return get_hundreds_text(number)


say(1234567)