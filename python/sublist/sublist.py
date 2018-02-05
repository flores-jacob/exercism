from itertools import islice, zip_longest

SUBLIST = "sublist"
EQUAL = "equal"
SUPERLIST = "superlist"
UNEQUAL = "unequal"


def check_lists(first_list, second_list):
    # Solution adapted from https://codereview.stackexchange.com/a/149942
    to_zip1 = ([*islice(second_list, start_index, None)] for start_index in range(len(first_list)))
    zipped_vals1 = [*zip_longest(*to_zip1)]

    to_zip2 = ([*islice(first_list, start_index, None)] for start_index in range(len(second_list)))
    zipped_vals2 = [*zip_longest(*to_zip2)]

    if first_list == second_list:
        return EQUAL
    elif (tuple(first_list) in zipped_vals1) or (first_list == []):
        return SUBLIST
    elif (tuple(second_list) in zipped_vals2) or (second_list == []):
        return SUPERLIST
    else:
        return UNEQUAL

