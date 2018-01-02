def square_of_sum(value):
    return sum([i for i in range(1, value + 1)]) ** 2


def sum_of_squares(value):
    return sum([i ** 2 for i in range(1, value + 1)])


def difference(value):
    return square_of_sum(value) - sum_of_squares(value)
