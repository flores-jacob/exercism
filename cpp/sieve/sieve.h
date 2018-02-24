#include <algorithm>

namespace sieve
{
    std::vector<int> primes(int n)
    {

        // Create a list of numbers up to the input, starting from the number 2
        std::vector<int> integer_list;
        for (int i=2; i<=n; i++){
            integer_list.push_back(i);
        };

        // Create a list of bool values that map to each number in the integer list
        std::vector<bool> is_prime_list(n, true);

        // Loop through the list of integers as divisors using their indices.
        // Loop a second time through the list to check mark off any numbers
        // that are divisible by these divisors

        // We start from zero, and end at n-2, because the integer_list starts
        // with the number 2; 0 and 1 are not in the list
        for (int divisor_index=0; divisor_index <= n-2; divisor_index++){
            int divisor_val = integer_list.at(divisor_index);
            // Loop once again through the list of integers as dividends.
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
        // it maps to a prime in the integer_list
        for (int i=0; i <= n - 2; i++){
            if (is_prime_list.at(i) == true){
                output_list.push_back(integer_list.at(i));
            }
        }

        return output_list;
    };

};