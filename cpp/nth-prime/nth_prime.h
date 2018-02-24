#include <vector>
#include <stdexcept>
#include <cmath>

namespace prime
{
    int nth (int nth_prime){
        if (nth_prime == 0){
            throw std::domain_error("must request at least the first prime number");
        };

        int int_containing_prime_est;

        if (nth_prime < 6){
            // the 6th prime is 13, so we just get values beneath that
            int_containing_prime_est = 12;
        }else{
            // estimate lifted from https://primes.utm.edu/howmany.html
            int_containing_prime_est  = nth_prime * (std::log(nth_prime) + std::log(std::log(nth_prime - 1)));
        }

        // Initialize a vector assuming all numbers are primes
        std::vector<bool> is_prime(int_containing_prime_est, true);

        // The first element which maps to 1 is tagged to be not prime
        is_prime.at(0) = false;

        // Mark multiples of each number as not prime
        for (int i=2; i <=int_containing_prime_est - 1; i++){
            for (int p=i + i; p <= int_containing_prime_est; p+=i ){
                is_prime.at(p - 1) = false;
            };
        };

        // count up to the nth prime and return the corresponding value
        int prime_count = 0;
        for (int k=0; k<int_containing_prime_est; k++){
            if (is_prime.at(k) == true){
                prime_count++;
                if (prime_count >= nth_prime){
                    return k + 1;
                };
            };
        };

    };

};