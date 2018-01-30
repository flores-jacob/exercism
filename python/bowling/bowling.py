
STRIKE = "strike"
SPARE = "spare"
OPEN = "open"


class BowlingGame(object):
    def __init__(self):
        self.frames = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.roll_count = 0
        self.current_frame = 0
        self.current_roll = OPEN
        self.previous_roll = OPEN
        self.the_roll_before = OPEN

    def roll(self, pins):
        self.roll_count += 1

        if self.the_roll_before == STRIKE:
            self.frames[self.current_frame - 2] += pins

        if self.previous_roll == SPARE:
            self.frames[self.current_frame - 1] += pins
        elif self.previous_roll == STRIKE:
            self.frames[self.current_frame - 1] += pins

        self.frames[self.current_frame] += pins

        if(self.frames[self.current_frame] == 10) and (self.roll_count == 1):
            self.current_roll = STRIKE
            # consider that the frame has ended if a strike was rolled
            self.roll_count = 2
        elif (self.frames[self.current_frame] == 10) and (self.roll_count == 2):
            self.current_roll = SPARE
        else:
            self.current_roll = OPEN

        if self.roll_count == 2:
            self.roll_count = 0
            self.current_frame += 1

        self.the_roll_before = self.previous_roll
        self.previous_roll = self.current_roll

    def score(self):
        print(self.frames)
        return sum(self.frames)
