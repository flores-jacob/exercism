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

    def sort(self):
        return_list = []
        for grade in sorted(self.roster):
            if self.roster[grade]:
                students_in_grade = tuple(sorted(self.roster[grade]))
                return_list.append((grade, students_in_grade))

        return return_list
