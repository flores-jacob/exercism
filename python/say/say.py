# python3


def in_words(number):
    ones_txt = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens_txt = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens_txt = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                 "nineteen"]

    # floor divide and get values of hundreds, tens, and ones
    hundreds = number // 100
    tens_and_ones = number - (hundreds * 100)
    tens = tens_and_ones // 10
    ones = int(tens_and_ones - (tens * 10))

    # if we have a value for the hundreds position, prepare the text for it
    if hundreds:
        hundreds_portion = " ".join([ones_txt[hundreds], "hundred"])
    else:
        hundreds_portion = ""

    # if the value for tens and ones value is in the teens, use the values in the teens list
    if 10 <= tens_and_ones <= 19:
        tens_and_ones_portion = teens_txt[ones]
    # if it's not in the teens, construct it from the tens and ones values
    else:
        tens_and_ones_portion_list = []
        if tens:
            tens_and_ones_portion_list.append(tens_txt[tens])
        if ones:
            tens_and_ones_portion_list.append(ones_txt[ones])

        if tens_and_ones_portion_list:
            tens_and_ones_portion = ("-".join(tens_and_ones_portion_list))
        else:
            tens_and_ones_portion = ""

    # if the hundreds and tens and ones both have values, combine them with the "and" word
    if hundreds and tens_and_ones:
        word_list = " and ".join([hundreds_portion, tens_and_ones_portion])
    # if it's just hundreds or just tens and ones, no need for the "and" connector
    else:
        word_list = "".join([hundreds_portion, tens_and_ones_portion])

    # join all the words from list form into string form
    return "".join(word_list)


def say(number):
    # make sure that input is proper
    if number == 0:
        return "zero"
    elif number < 0:
        raise ValueError("Input value cannot be negative")
    elif number > 999999999999:
        raise ValueError("input value should not exceed 999,999,999,999")

    # compute the values for billions, millions, thousands, and hundreds
    billions = number // 1000000000
    millions = (number - (billions * 1000000000)) // 1000000
    thousands = (number - (billions * 1000000000) - (millions * 1000000)) // 1000
    hundreds = number - (billions * 1000000000) - (millions * 1000000) - (thousands * 1000)

    number_str_list = []

    # feed each value into the get_hundreds_text function to obtain text equivalent of their chunk
    # also, append billion, million, or thousand for the respective values
    if billions:
        number_str_list.extend([in_words(billions), "billion"])
    if millions:
        number_str_list.extend([in_words(millions), "million"])
    if thousands:
        number_str_list.extend([in_words(thousands), "thousand"])
    # add the word "and" if the hundreds value is less than 100, and if we have other higher values
    if 0 < hundreds < 100 and (thousands or millions or billions):
        number_str_list.extend(["and", in_words(hundreds)])
    # otherwise, just get the normal text
    else:
        number_str_list.extend([in_words(hundreds)])
    # combine the constructed list into string format, and remove any trailing whitespace.
    return " ".join(number_str_list).strip()
