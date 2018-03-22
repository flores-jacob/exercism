def is_equilateral(sides):
    if any(sides) <= 0:
        return False
    else:
        return (sides[0] == sides[1]) and (sides[1] == sides[2])


def is_isosceles(sides):
    pass


def is_scalene(sides):
    pass
