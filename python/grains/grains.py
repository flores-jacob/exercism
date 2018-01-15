def on_square(integer_number):
    if (integer_number < 1) or (integer_number > 64):
        raise ValueError("input square should be between 1 and 64")

    square_val = 1
    for i in range(2, integer_number + 1):
        square_val *= 2
    return square_val


def total_after(integer_number):
    if (integer_number < 1) or (integer_number > 64):
        raise ValueError("input square should be between 1 and 64")

    total_grains = 0

    for i in range(1, integer_number + 1):
        total_grains += on_square(i)

    return total_grains
