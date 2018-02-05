SUBLIST = "sublist"
EQUAL = "equal"
SUPERLIST = "superlist"
UNEQUAL = "unequal"


def check_lists(first_list, second_list):
    if first_list == second_list:
        return EQUAL

    for sublist in (second_list[i:i + len(first_list)] for i in range(len(second_list))):
        if first_list == sublist:
            return SUBLIST

    for sublist in (first_list[i:i + len(second_list)] for i in range(len(first_list))):
        if second_list == sublist:
            return SUPERLIST

    return UNEQUAL
