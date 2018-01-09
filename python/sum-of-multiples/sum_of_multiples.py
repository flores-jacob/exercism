def sum_of_multiples(limit, multiples):
    multiple_list = []
    for i in range(1, limit):
        for multiple in multiples:
            if i % multiple == 0:
                multiple_list.append(i)
                break

    return sum(multiple_list)