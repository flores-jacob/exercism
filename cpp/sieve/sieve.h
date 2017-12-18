#include <algorithm>

namespace sieve
{
    std::vector<int> primes(int n)
    {

        // create a list of numbers up to the input, starting from the number 2
        std::vector<int> integer_list;
        for (int i=2; i<=n; i++){
            integer_list.push_back(i);
        };

        // iterate through the list for each element as a divisor
        for (int divisor: integer_list){
            // if any other element in the list can be divided by the divisor:
            for (int elem: integer_list){
                // if the integer is divisible by the current divisor, and the divisor is not the same as the integer
                // as the number, then it is not a prime number and we remove it from the vector
                if ((elem % divisor == 0) && (elem != divisor)){
                    integer_list.erase(std::remove(integer_list.begin(), integer_list.end(), elem), integer_list.end());
                };
            };
        };

        // return the modified list
        return integer_list;
    };

};