def prime_factors(natural_number):
    factor_list = []
    candidate_factor = 2

    while candidate_factor <= natural_number:
        if natural_number % candidate_factor == 0:
            factor_list.append(candidate_factor)
            natural_number /= candidate_factor
        else:
            candidate_factor += 1

    return factor_list
