def verify(isbn):
    # Remove any dashes
    no_dashes = isbn.replace("-", "")
    # Make sure that string length is correct
    if len (no_dashes) != 10:
        return False

    initial_nine_nums = no_dashes[:9]
    final_num = no_dashes[9]

    total = 0
    # Loop through the first 9 numbers, multiply by their factors, and
    # add to the total if they are digits
    for i in range(9):
        if initial_nine_nums[i].isdigit():
            total += int(initial_nine_nums[i]) * (10 - i)
        else:
            return False

    # Add the correct value for the 10th and last digit
    if final_num == 'X':
        total += 10
    elif final_num.isdigit():
        total += int(final_num)
    else:
        return False

    # Return True or False if the final number total is divisible by 11 or not
    return total % 11 == 0