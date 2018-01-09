def sum_of_multiples(limit, multiples):
    if not multiples:
        return 0

    multiple_sum = 0
    for i in range(1, limit):
        for multiple in multiples:
            if i % multiple == 0:
                multiple_sum += i
                break

    return multiple_sum