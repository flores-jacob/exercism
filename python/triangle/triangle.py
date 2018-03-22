def is_valid_triangle(sides):
    if any(sides) <= 0:
        return False
    elif not((sides[0] + sides[1]) >= sides[2]) \
            or not ((sides[0] + sides[2]) >= sides[1]) \
            or not ((sides[1] + sides[2]) >= sides[0]):
        return False
    else:
        return True


def is_equilateral(sides):
    if is_valid_triangle(sides):
        return (sides[0] == sides[1]) and (sides[1] == sides[2])
    else:
        return False


def is_isosceles(sides):
    if is_valid_triangle(sides):
        return (sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2])
    else:
        return False


def is_scalene(sides):
    if is_valid_triangle(sides):
        return (sides[0] != sides[1]) and (sides[0] != sides[2]) and (sides[1] != sides[2])
    else:
        return False
