import copy

COLOR = "color"
colors = ["red", "green", "ivory", "yellow", "blue"]
RED, GREEN, IVORY, YELLOW, BLUE = colors

NATIONALITY = "nationality"
nationalities = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
ENGLISHMAN, SPANIARD, UKRAINIAN, NORWEGIAN, JAPANESE = nationalities

PET = "pet"
pets = ["dog", "snails", "fox", "horse", "zebra"]
DOG, SNAILS, FOX, HORSE, ZEBRA = pets

DRINK = "drink"
drinks = ["coffee", "tea", "milk", "orange juice", "water"]
COFFEE, TEA, MILK, ORANGE_JUICE, WATER = drinks

SMOKES = "smokes"
smokes = ["Old Gold", "Kools", "Chesterfields", "Lucky Strike", "Parliaments"]
OLD_GOLD, KOOLS, CHESTERFIELDS, LUCKY_STRIKE, PARLIAMENTS = smokes

house_template = {
    COLOR: colors,
    NATIONALITY: nationalities,
    PET: pets,
    DRINK: drinks,
    SMOKES: smokes
}


def remove_if_present(source_list, item):
    if item in source_list: source_list.remove(item)


def simple_location_based_fact(house_list, house_index, predicate_key, predicate_value):
    # Remove the value from all houses
    for house in house_list:
        remove_if_present(house[predicate_key], predicate_value)

    # Assign the correct value to the given house
    house_list[house_index][predicate_key] = [predicate_value]


# if house on the left's premise is so and so, then house predicate is so and so
def left_right_fact(house_list, left_house_key, left_house_value, right_house_key, right_house_value):
    # leftmost house has no house on the left, so remove the
    # right_house_value from it
    remove_if_present(house_list[0][right_house_key], right_house_value)

    for house_index in range(1, 4):

        # If the right house characteristic is not available to this house:
        if right_house_value not in house_list[house_index][right_house_key]:
            # Then remove the left house characteristic from the house on the left
            remove_if_present(house_list[house_index - 1][left_house_key], left_house_value)

        # If the characteristic is not available on the house on the left:
        if left_house_value not in house_list[house_index - 1][left_house_key]:
            # Remove the right house value on the house on the current house
            remove_if_present(house_list[house_index][right_house_key], right_house_value)

        # If the left house characteristic is not available on this house:
        if left_house_value not in house_list[house_index][left_house_key]:
            # Remove the right house value on the house on the right
            remove_if_present(house_list[house_index + 1][right_house_key], right_house_value)

    # Rightmost house does not have a house on its right, therefore, we
    # remove the left house value from it
    remove_if_present(house_list[4][left_house_key], left_house_value)


def house_beside_fact(house_list, premise_key, premise_value, predicate_key, predicate_value):
    # If the premise can be found on the first element:
    if house_list[0][premise_key] == [premise_value]:
        # Then the predicate is true for the second element
        house_list[1][predicate_key] = [predicate_value]

    for index in range(1, 4):
        match_on_left = house_list[index - 1][premise_key] == [premise_value]
        match_on_right = house_list[index + 1][premise_key] == [premise_value]

        if match_on_left:
            for house in house_list[index + 1:]:
                remove_if_present(house[predicate_key], predicate_value)

        if match_on_right:
            for house in house_list[:index - 1]:
                remove_if_present(house[predicate_key], predicate_value)

    # If the premise can be found on the last element
    if house_list[4][premise_key] == [premise_value]:
        # Then the predicate can be found on the 2nd to the last element
        house_list[3][predicate_key] = [predicate_value]

    # If value is not present in house beside the first house
    if premise_value not in house_list[1][premise_key]:
        # remove the predicate value from it
        remove_if_present(house_list[0][predicate_key], predicate_value)

    for index in range(1, 4):
        present_on_the_left = premise_value in house_list[index - 1][premise_key]
        present_on_the_right = premise_value in house_list[index + 1][premise_key]

        # IF the premise is not on the left or right, remove the predicate
        if not (present_on_the_left) and not (present_on_the_right):
            remove_if_present(house_list[index][predicate_key], predicate_value)

    # If value is not present in house beside the last house
    if premise_value not in house_list[3][premise_key]:
        # remove the predicate value from it
        remove_if_present(house_list[4][predicate_key], predicate_value)


def same_house_fact(house_list, first_fact_key, first_fact_value, second_fact_key, second_fact_value):
    for house in house_list:
        if house[first_fact_key] == [first_fact_value]:
            house[second_fact_key] = [second_fact_value]

        if house[second_fact_key] == [second_fact_value]:
            house[first_fact_key] = [first_fact_value]

    for house in house_list:
        if first_fact_value not in house[first_fact_key]:
            remove_if_present(house[second_fact_key], second_fact_value)

    for house in house_list:
        if second_fact_value not in house[second_fact_key]:
            remove_if_present(house[first_fact_key], first_fact_value)


def eliminate(house_list):
    for house_index in range(0, 5):
        other_houses = [0, 1, 2, 3, 4]
        other_houses.remove(house_index)

        keys = house_list[house_index].keys()
        for key in keys:
            # If an answer has been deduced for a single field, then remove
            # its occurrences in the other houses
            if len(house_list[house_index][key]) == 1:
                deduced_answer = house_list[house_index][key][0]
                for other_house_index in other_houses:
                    remove_if_present(house_list[other_house_index][key], deduced_answer)


def clues(houses):
    same_house_fact(houses, NATIONALITY, ENGLISHMAN, COLOR, RED)
    same_house_fact(houses, NATIONALITY, SPANIARD, PET, DOG)
    same_house_fact(houses, DRINK, COFFEE, COLOR, GREEN)
    same_house_fact(houses, DRINK, TEA, NATIONALITY, UKRAINIAN)

    left_right_fact(houses, COLOR, IVORY, COLOR, GREEN)
    # left_right_fact(houses, COLOR, GREEN, COLOR, IVORY)

    same_house_fact(houses, SMOKES, OLD_GOLD, PET, SNAILS)
    same_house_fact(houses, SMOKES, KOOLS, COLOR, YELLOW)
    simple_location_based_fact(houses, 2, DRINK, MILK)
    simple_location_based_fact(houses, 0, NATIONALITY, NORWEGIAN)

    house_beside_fact(houses, SMOKES, CHESTERFIELDS, PET, FOX)
    house_beside_fact(houses, PET, FOX, SMOKES, CHESTERFIELDS)

    house_beside_fact(houses, SMOKES, KOOLS, PET, HORSE)
    house_beside_fact(houses, PET, HORSE, SMOKES, KOOLS)

    same_house_fact(houses, SMOKES, LUCKY_STRIKE, DRINK, ORANGE_JUICE)
    same_house_fact(houses, NATIONALITY, JAPANESE, SMOKES, PARLIAMENTS)

    house_beside_fact(houses, NATIONALITY, NORWEGIAN, COLOR, BLUE)
    house_beside_fact(houses, COLOR, BLUE, NATIONALITY, NORWEGIAN, )

    return houses


def iterate_through_clues(house_list):
    value_count = 0
    for house in house_list:
        for key in house.keys():
            value_count += len(house[key])

    new_count = 0

    while value_count != new_count:
        value_count = new_count
        new_count = 0
        clues(house_list)
        eliminate(house_list)
        for house in house_list:
            for key in house.keys():
                new_count += len(house[key])
        # Loops around 4 times


# Initialize houses
house_list = [copy.deepcopy(house_template) for i in range(5)]

# Run the houses through the clues
iterate_through_clues(house_list)

# The color Red can't possibly be found on index 3, inbetween ivory and
# green
remove_if_present(house_list[3][COLOR], RED)
# Choosing OJ and Lucky Strike on index 2 would prevent the insertion of
# either the Japanese or Ukrainian, as such, we disqualify them from
# that index
remove_if_present(house_list[1][DRINK], ORANGE_JUICE)
# OJ and Lucky strike can only be placed on two indices, index 3 or index 4
# Here we use index 3 and obtain the desired results
simple_location_based_fact(house_list, 3, DRINK, ORANGE_JUICE)

# Run through the clues once again
iterate_through_clues(house_list)

for house in house_list:
    print(house[NATIONALITY], house[DRINK], house[COLOR], house[PET], house[SMOKES])


def drinks_water():
    for house in house_list:
        if house[DRINK] == [WATER]:
            return house[NATIONALITY][0]

    return None


def owns_zebra():
    for house in house_list:
        if house[PET] == [ZEBRA]:
            return house[NATIONALITY][0]

    return None
