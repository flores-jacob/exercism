# Globals for the bearings
# Change the values as you see fit
EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return (self.x, self.y)

    def turn_right(self):
        self.bearing += 1
        if self.bearing > 3:
            self.bearing = 0

    def turn_left(self):
        self.bearing -= 1
        if self.bearing < 0:
            self.bearing = 3

    def advance(self):
        if self.bearing == 0:
            self.y += 1
        elif self.bearing == 1:
            self.x += 1
        elif self.bearing == 2:
            self.y -= 1
        elif self.bearing == 3:
            self.x -= 1

    def simulate(self, move_sequence):
        for char in move_sequence:
            if char == "A":
                self.advance()
            elif char == "L":
                self.turn_left()
            if char == "R":
                self.turn_right()

