#include <vector>

namespace prime_factors
{
    std::vector<int> of (int input)
    {
        std::vector<int> prime_factor_vector;

        for (int i=2; i<=input; i++){
            if (input % i == 0){
                prime_factor_vector.push_back(i);
                input = input/i;
                std::vector<int> recursive_factors = of(input);
                // vector concatenation https://stackoverflow.com/a/3177254
                prime_factor_vector.insert(prime_factor_vector.end(), recursive_factors.begin(), recursive_factors.end());
                break;
            };
        };

        return prime_factor_vector;
    };
};