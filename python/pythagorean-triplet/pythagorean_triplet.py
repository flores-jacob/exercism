from math import gcd
from operator import itemgetter


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
    # Get all primitive triplets
    # keep on multiplying each primitive triplet until its max value
    # exceeds the range end
    primitive_results = set()
    max_triplet_val = 0
    num = range_start
    while max_triplet_val <= range_end:
        new_triplets = primitive_triplets(num)
        if new_triplets:
            max_triplet_val = max(new_triplets, key=itemgetter(2))[2]
        if max_triplet_val <= range_end:
            primitive_results = primitive_results.union(new_triplets)
        num += 1

    triplet_results = set()
    for triplet in primitive_results:
        for multiplier in range(1, range_end):
            new_triplet = (triplet[0] * multiplier, triplet[1] * multiplier, triplet[2] * multiplier)
            if new_triplet[2] <= range_end:
                triplet_results.add(new_triplet)
            else:
                break

    return triplet_results


def is_triplet(triplet):
    sorted_triplet = sorted(triplet)
    return sorted_triplet[0] ** 2 + sorted_triplet[1] ** 2 == sorted_triplet[2] ** 2
