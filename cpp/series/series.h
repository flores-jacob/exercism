#include <string>
#include <vector>
#include <iostream>
namespace series
{
    std::vector<int> digits(std::string digits_string)
    {
        std::vector<int> integer_vector;

        for (int i=0; i<digits_string.size(); i++) {
            // cast char to int
            int elem = digits_string.at(i);
            // subtract 48 to transform value from char to int
            integer_vector.push_back(elem - 48);
        };

        return integer_vector;
    };
};