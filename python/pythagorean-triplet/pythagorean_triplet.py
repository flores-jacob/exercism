from math import gcd


def primitive_triplets(number_in_triplet):
    if number_in_triplet % 2 == 0:
        m_x_n = number_in_triplet / 2
    else:
        raise ValueError("Number should be even")
    # Generate all pairs of numbers that result to the product of
    # number_in_triplet/2
    # Make sure that the greater factor is element 0, and the lesser
    # factor is element 1
    # Adapted from https://stackoverflow.com/a/5505024
    factor_pairs = (sorted([i, int(m_x_n / i)], reverse=True) for i in range(1, int(m_x_n ** 0.5) + 1) if m_x_n % i == 0)

    triplet_results = set()
    for m, n in factor_pairs:
        if gcd(m, n) != 1:
            continue
        triplet = tuple(sorted([(m ** 2 - n ** 2), number_in_triplet, m ** 2 + n ** 2]))
        triplet_results.add(triplet)

    return triplet_results


def triplets_in_range(range_start, range_end):
    triplet_results = set()
    for b in range(0, range_end, 4):
        prim_triplets = primitive_triplets(b)
        for k in range(1, range_end + 1):
            for a, b, c in prim_triplets:
                if k * a >= range_start and k * c <= range_end:
                    triplet_results.add((k * a, k * b, k * c))
    return triplet_results


def is_triplet(triplet):
    sorted_triplet = sorted(triplet)
    return sorted_triplet[0] ** 2 + sorted_triplet[1] ** 2 == sorted_triplet[2] ** 2
