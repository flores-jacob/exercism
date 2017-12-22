#include <vector>
#include <iostream>
namespace prime
{
    int nth (int nth_prime){
        int current_prime;
        int current_prime_count = 0;
        std::vector<int> discovered_primes;

        int current_int = 2;

        // while we have not yet discovered up to n prime numbers
//        while (current_prime_count < nth_prime){
        while (discovered_primes.size() < nth_prime){
            // assume that current int is not divisible
            bool divisible = false;
            // we loop through each of the primes we have already discovered
            for (int prime: discovered_primes){
                // we check if the current int in question is divisible by any of the already discovered ones
                if (current_int % prime == 0){
                    divisible = true;
                    // if it is divisible, then we increase the int count by one
                    current_int += 1;
                    // and we move on to the next item in the while loop
                    break;
                }
            };
            // if current int is not divisible by any of the previously discovered primes
            // then we add it to the discovered primes vector, and increase current_prime_count by one
            if (divisible == false){
                discovered_primes.push_back(current_int);
                std::cout << "current prime " << current_int << std::endl;
            };
        };
        std::cout << std::endl;
        return discovered_primes.back();
    };
};