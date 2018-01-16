def verify(isbn):
    # Remove any dashes
    no_dashes = isbn.replace("-", "")
    # Make sure that string length is correct
    if len (no_dashes) != 10:
        return False
    initial_nine_nums = no_dashes[:9]
    final_num = no_dashes[9]

    total = 0
    for i in range(9):
        try:
            total += int(initial_nine_nums[i]) * (10 - i)
        # Return False one of the numbers can't be cast into an int
        except ValueError:
            return False

    if final_num == 'X':
        total += 10
    else:
        try:
            total += int(final_num)
        # Return False if the final number can't be cast into an int
        except ValueError:
            return False

    # return False if the final number total is not divisible by 11
    if total % 11 == 0:
        return True
    else:
        return False