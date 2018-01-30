

class BowlingGame(object):
    def __init__(self):
        self.frames = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.current_roll = 0
        self.previous_roll = 0
        self.the_roll_before = 0

    def roll(self, pins):
        pass

    def score(self):
        return sum(self.frames)
