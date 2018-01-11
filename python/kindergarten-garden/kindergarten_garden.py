class Garden(object):
    students = sorted([ "Alice", "Bob", "Charlie", "David",
                "Eve", "Fred", "Ginny", "Harriet",
                "Ileana", "Joseph", "Kincaid", "Larry"])

    plant_names_dict = {"V": "Violets", "R": "Radishes", "C": "Clover", "G": "Grass"}

    def __init__(self, diagram, students=students):
        self.student_list = sorted(students)
        self.top_plants, self.bottom_plants = diagram.split()

    def plants(self, student_name):
        student_index = self.student_list.index(student_name)
        plant_index = student_index * 2
        students_plants = self.top_plants[plant_index: plant_index + 2] + self.bottom_plants[plant_index: plant_index + 2]

        return[Garden.plant_names_dict[plant_letter] for plant_letter in students_plants]