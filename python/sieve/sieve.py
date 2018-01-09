def sieve(limit):
    
    desired_range = range(2, limit + 1)
    
    not_primes = set()

    for current_candidate in desired_range:
        if current_candidate in not_primes:
            continue

        for succeeding_num in desired_range:
            if (succeeding_num % current_candidate == 0) and (current_candidate != succeeding_num):
                not_primes.add(succeeding_num)

    prime_list = sorted(list(set(desired_range) - not_primes))

    return prime_list

