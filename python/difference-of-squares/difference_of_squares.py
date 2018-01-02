def square_of_sum(value):
    return sum([i + 1 for i in range(value)]) ** 2


def sum_of_squares(value):
    return sum([(i + 1) ** 2 for i in range(value)])


def difference(value):
    return square_of_sum(value) - sum_of_squares(value)
