SUBLIST = "sublist"
EQUAL = "equal"
SUPERLIST = "superlist"
UNEQUAL = "unequal"


def check_lists(first_list, second_list):
    first_string = " ".join(str(i) for i in first_list)
    second_string = " ".join(str(j) for j in second_list)

    if first_list == second_list:
        return EQUAL
    elif first_string in second_string:
        return SUBLIST
    elif second_string in first_string:
        return SUPERLIST
    else:
        return UNEQUAL

