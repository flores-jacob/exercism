def get_factors(natural_number):
    factor_list = []
    candidate_factor = 1

    while candidate_factor < natural_number:
        if natural_number % candidate_factor == 0:
            factor_list.append(candidate_factor)
        candidate_factor += 1

    return factor_list


def classify(number):

    if number <= 0:
        raise ValueError("Input number should be positive")

    aliquot_sum = sum(get_factors(number))

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    elif aliquot_sum < number:
        return "deficient"
