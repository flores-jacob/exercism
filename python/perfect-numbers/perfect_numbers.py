def classify(number):

    if number <= 0:
        raise ValueError("Input number should be positive")
    elif number == 1:
        return "deficient"

    aliquot_sum = 1
    candidate_factor = 2
    candidate_factor_pair = number

    while candidate_factor < candidate_factor_pair:
        if number % candidate_factor == 0:
            candidate_factor_pair = int(number/candidate_factor)

            aliquot_sum += candidate_factor
            if candidate_factor != candidate_factor_pair:
                aliquot_sum += candidate_factor_pair
        candidate_factor += 1

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    elif aliquot_sum < number:
        return "deficient"
