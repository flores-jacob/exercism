def verify(isbn):
    # Remove any dashes
    no_dashes = isbn.replace("-", "")
    # Make sure that string length is correct
    if len(no_dashes) != 10:
        return False

    initial_nine_nums = no_dashes[:9]
    final_num = no_dashes[9]

    # Ensure that all chars are digits
    if not initial_nine_nums.isdigit():
        return False

    # Get sum of first nine numbers
    total = sum([int(num) * (10 - index) for index, num in enumerate(initial_nine_nums)])

    # Add the correct value for the 10th and last digit
    if final_num == 'X':
        total += 10
    elif final_num.isdigit():
        total += int(final_num)
    else:
        return False

    # Return True or False if the final number total is divisible by 11 or not
    return total % 11 == 0