import math


class Allergies(object):
    allergen_masterlist = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]

    def __init__(self, score):
        self.score = score
        self.allergy_list = []

        while score:
            allergen_index = int(math.floor(math.log(score, 2)))
            if allergen_index < len(Allergies.allergen_masterlist):
                self.allergy_list.append(Allergies.allergen_masterlist[allergen_index])
            score -= pow(2, allergen_index)

    def is_allergic_to(self, item):
        return item in self.allergy_list

    @property
    def lst(self):
        return self.allergy_list
