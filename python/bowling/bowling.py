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

        self.total_rolls = 0

    def roll(self, pins):
        if pins < 0:
            raise ValueError("Rolls cannot have a score less than 0")
        elif pins > 10:
            raise ValueError("Rolls cannot have a score greater than 10")

        if self.current_frame > 9:
            raise IndexError("Cannot roll if there are already 10 frames")

        self.roll_count += 1

        # Add the fallen pins to the score
        self.frames[self.current_frame] += pins

        # Assign whether or not the frame is a strike, a spare, or an open
        if (self.frames[self.current_frame] == 10) and (self.roll_count == 1):
            self.current_roll = STRIKE
        elif (self.frames[self.current_frame] == 10) and (self.roll_count == 2):
            self.current_roll = SPARE
        elif (pins == 10) and (self.roll_count == 2) and (self.current_frame == 9):
            self.current_roll = STRIKE
        else:
            self.current_roll = OPEN

        # For frames 0 to 8, and the first roll of 9, the scoring is the same
        if (self.current_frame < 9) or ((self.current_frame == 9) and (self.roll_count == 1)):
            if self.the_roll_before == STRIKE:
                self.frames[self.current_frame - 2] += pins

            if self.previous_roll == SPARE:
                self.frames[self.current_frame - 1] += pins
            elif self.previous_roll == STRIKE:
                self.frames[self.current_frame - 1] += pins
        # However, on the second roll of 9, the scoring is different
        elif (self.current_frame == 9) and (self.roll_count == 2):
            if self.the_roll_before == STRIKE:
                self.frames[self.current_frame - 1] += pins

        print(self.frames)

        # if (self.current_frame == 9) and (self.roll_count == 3):
        #     if (self.the_roll_before == STRIKE) and (self.previous_roll == OPEN) and (pins > 0):
        #         raise ValueError("Second roll should be a strike")

        if (self.current_frame != 9) and (self.current_roll == STRIKE):
            # If this is not the final frame, and we have a strike, we
            # end the frame
            self.roll_count = 2

        self.total_rolls += self.roll_count

        # if (self.current_frame == 9) and (self.roll_count == 3):
        #     if not ((self.previous_roll == SPARE) or (self.the_roll_before == STRIKE)):
        #         raise ValueError("First frame must be a strike or previous roll a spare")
        #     self.current_frame += 1

        if self.current_frame != 9:
            if self.roll_count == 2:
                if self.frames[self.current_frame] > 10:
                    raise ValueError("A frame cannot have more than 10 pts")
                self.roll_count = 0
                self.current_frame += 1
        elif self.current_frame == 9:
            print(self.current_frame, self.roll_count, self.the_roll_before, self.previous_roll, self.current_roll)

            if self.roll_count == 3 and (self.the_roll_before != STRIKE) and (self.previous_roll != SPARE):
                raise IndexError("Ten frames already complete")


        self.the_roll_before = self.previous_roll
        self.previous_roll = self.current_roll

    def score(self):
        # print(self.frames)
        if self.current_frame < 9:
            raise IndexError("Incomplete games cannot be scored")
        elif self.current_roll == STRIKE:
            raise IndexError("Bonus roll for strike has to be rolled first")
        elif self.current_roll == SPARE:
            raise IndexError("Bonus roll for spare has to be rolled first")
        return sum(self.frames)
