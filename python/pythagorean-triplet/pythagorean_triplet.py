from math import gcd
from itertools import combinations

def primitive_triplets(number_in_triplet):
    if number_in_triplet % 2 == 0:
        m_x_n = number_in_triplet / 2
    else:
        raise ValueError("Number should be even")
    # generate all pairs of numbers that result to the product of number_in_triplet/2
    # adapted from https://stackoverflow.com/a/5505024
    factor_pairs = ((i, int(m_x_n / i)) for i in range(1, int(m_x_n ** 0.5) + 1) if m_x_n % i == 0)
    # filter the list in such that the greater number minus the lesser number results
    # in an odd difference
    factor_pairs = filter(lambda x: (max(x) - min(x)) % 2 != 0, factor_pairs)
    # Loop through each pair, and check which ones are coprime, make sure arrangement is greater
    # number is the first element, and lesser number is second element
    factor_pairs = (sorted(pair) for pair in factor_pairs if gcd(pair[0], pair[1]) == 1)
    # return triplet values as a set of tuples
    # a = (m ^ 2 - n ^ 2), b = 2 * m * n and c = (m ^ 2 + n ^ 2)
    return set(tuple(sorted(((m ** 2) - (n ** 2), number_in_triplet, (m ** 2) + (n ** 2)))) for n, m in factor_pairs)


def triplets_in_range(range_start, range_end):
    return set(triplet for triplet in combinations(range(range_start, range_end + 1), 3) if is_triplet(triplet))


def is_triplet(triplet):
    sorted_triplet = sorted(triplet)
    return sorted_triplet[0] ** 2 + sorted_triplet[1] ** 2 == sorted_triplet[2] ** 2
