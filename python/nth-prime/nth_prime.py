def nth_prime(positive_number):
        if positive_number == 0:
            raise ValueError("Input should be a positive number")

        discovered_primes = []
        current_int = 2

        # while we have not yet discovered up to n prime numbers
        while len(discovered_primes) < positive_number:
            # assume that current int is not divisible
            divisible = False
            # we loop through each of the primes we have already discovered
            for prime in discovered_primes:
                # we check if the current int in question is divisible by any of the already discovered ones
                if current_int % prime == 0:
                    divisible = True
                    # if it is divisible, then we increase the int count by one
                    current_int += 1
                    # and we move on to the next item in the while loop
                    break

            # if current int is not divisible by any of the previously discovered primes
            # then we add it to the discovered primes vector, and increase current_prime_count by one
            if divisible is False:
                discovered_primes.append(current_int)
        return discovered_primes[-1]

