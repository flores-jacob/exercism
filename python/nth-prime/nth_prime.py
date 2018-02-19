def nth_prime(positive_number):
        if positive_number == 0:
            raise ValueError("Input should be a positive number")

        discovered_primes = []
        current_int = 2

        # while we have not yet discovered up to n prime numbers
        while len(discovered_primes) < positive_number:

            # If all of the currently discovered primes cannot evenly
            # divide the current_int, then we add current_int as a prime
            if all(current_int % prime != 0 for prime in discovered_primes):
                discovered_primes.append(current_int)

            current_int += 1

        return discovered_primes[-1]

