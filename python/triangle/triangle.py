def is_valid_triangle(func):
    def inner(sides):
        if any(sides) <= 0:
            return False
        elif not((sides[0] + sides[1]) >= sides[2]) \
                or not ((sides[0] + sides[2]) >= sides[1]) \
                or not ((sides[1] + sides[2]) >= sides[0]):
            return False
        return func(sides)
    return inner


@is_valid_triangle
def is_equilateral(sides):
    return (sides[0] == sides[1]) and (sides[1] == sides[2])


@is_valid_triangle
def is_isosceles(sides):
    return (sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2])


@is_valid_triangle
def is_scalene(sides):
    return (sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[1] != sides[2])
