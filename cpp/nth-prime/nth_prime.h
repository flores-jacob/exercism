#include <vector>

namespace prime
{
    int nth (int nth_prime){
        int current_prime;
        int current_prime_count;
        std::vector<int> discovered_primes;

        int current_int = 2;

        while (current_prime_count < nth_prime){
            for (int prime: discovered_primes){
                if (current_int % prime == 0){
                    current_int += 1;
                    break;
                };
            };

            // if current int is not divisible by any of the previously discovered primes
            // then we add it to the discovered primes vector, and increase current_prime_count by one
            discovered_primes.push_back(current_int);
            current_prime_count += 1;
        };

        return current_int;

    };
};