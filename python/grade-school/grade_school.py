class School(object):
    def __init__(self, name):
        self.name = name
        self.roster = {}

        for i in range(1, 10):
            self.roster[i] = set()

    def grade(self, grade_num):
        return self.roster[grade_num]

    def add(self, student_name, grade_number):
        self.roster[grade_number].add(student_name)
