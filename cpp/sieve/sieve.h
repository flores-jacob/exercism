#include <algorithm>

namespace sieve
{
    std::vector<int> primes(int n)
    {

        // Create a list of bool values that map to each number
        std::vector<bool> is_prime_list(n, true);

        // Loop through the each of the elements in the is_prime_list
        for (int divisor_index=0; divisor_index <= n-2; divisor_index++){
            // Assign the divisor value as 2 + the index
            int divisor_val = 2 + divisor_index;
            // Loop through the integers starting from 2 up to n as dividends.
            // Starting with the value of the current divisor + divisor_val,
            // we increment by the value of the divisor, and all dividends
            // found this way are divisible by the divisor and are non-prime
            for (int dividend_index=divisor_index + divisor_val; dividend_index <= n-2; dividend_index += divisor_val){
                is_prime_list.at(dividend_index) = false;
            };
        };

        // Prepare the output_list
        std::vector<int> output_list;

        // Loop through the is_prime_list; if the element is true, then
        // it maps to a prime number.
        // Its index + 2 represents this prime number
        for (int i=0; i <= n - 2; i++){
            if (is_prime_list.at(i) == true){
                output_list.push_back(2 + i);
            }
        }

        return output_list;
    };

};