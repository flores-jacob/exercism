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
    return is_valid_triangle(sides) \
           and (sides[0] == sides[1]) \
           and (sides[1] == sides[2])


def is_isosceles(sides):
    return is_valid_triangle(sides) \
           and (
                   (sides[0] == sides[1])
                   or (sides[0] == sides[2])
                   or (sides[1] == sides[2])
           )


def is_scalene(sides):
    return is_valid_triangle(sides) \
           and (sides[0] != sides[1]) \
           and (sides[0] != sides[2]) \
           and (sides[1] != sides[2])
