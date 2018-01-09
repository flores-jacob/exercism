# python3

def say(number):
    if number == 0:
        return "zero"

    ones_txt = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens_txt = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens_txt = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
             "nineteen"]

    # floor divide
    hundreds = number // 100
    tens_and_ones  = number - (hundreds * 100)
    tens = tens_and_ones // 10
    ones = tens_and_ones - (tens * 10)

    in_words = []

    if hundreds:
        in_words.extend([ones[hundreds], " hundred"])

    if 10 <= tens_and_ones <= 19:
        print(ones)
        print(teens_txt[ones])
        in_words.extend([teens_txt[ones]])
    elif ones:
        in_words.extend([ones_txt[ones]])

    return "".join(in_words)