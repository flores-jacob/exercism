def distance(strand_a, strand_b):
    ham_distance = 0

    if len(strand_a) != len(strand_b):
        raise ValueError("strand length mismatch")

    for i in range(len(strand_a)):
        # print(strand_a[i], strand_b[i])
        if strand_a[i] != strand_b[i]:
            ham_distance += 1

    return ham_distance
