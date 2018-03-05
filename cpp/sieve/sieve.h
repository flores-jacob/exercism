#include <algorithm>

namespace sieve
{
    std::vector<int> primes(int n)
    {

        // Create a list of bool values that map to each number 0 to n
        std::vector<bool> is_prime_list(n + 1, true);

        // Mark 0 and 1 as non-prime numbers
        is_prime_list.at(0) = false;
        is_prime_list.at(1) = false;

        // Loop through the each of the elements in the is_prime_list,
        // starting from the number 2
        for (int divisor=2; divisor <= n; divisor++){
            // If the divisor is a non-prime number, skip and move to the
            // next divisor
            if (!is_prime_list[divisor]){
                continue;
            };

            // Loop through the integers starting from 2 up to n as dividends.
            // Starting with the value of the current divisor * 2,
            // we increment by the value of the divisor, and all dividends
            // found this way are divisible by the divisor and are non-prime
            for (int dividend=divisor + divisor; dividend <= n; dividend += divisor){
                is_prime_list.at(dividend) = false;
            };
        };

        // Prepare the output_list
        std::vector<int> output_list;

        // Loop through the is_prime_list; if the element is true, then
        // it maps to a prime number.
        for (int i=0; i <= n; i++){
            if (is_prime_list.at(i)){
                output_list.push_back(i);
            }
        }

        return output_list;
    };

};