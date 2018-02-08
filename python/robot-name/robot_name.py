import random


class Robot(object):
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    taken_names = []

    def __init__(self):
        self.name = Robot.generate_name(self)

    def generate_name(self):
        new_name = "".join([random.choice(Robot.letters),
                        random.choice(Robot.letters),
                        random.choice(Robot.numbers),
                        random.choice(Robot.numbers),
                        random.choice(Robot.numbers),])

        if new_name not in Robot.taken_names:
            Robot.taken_names.append(new_name)
        else:
            new_name = Robot.generate_name(self)

        return new_name

    def reset(self):
        self.name = Robot.generate_name(self)
