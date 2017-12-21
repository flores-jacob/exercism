#include <string>
#include <vector>
#include <stdexcept>

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

    std::vector<std::vector<int>> slice(std::string digits_string, int series_length)
    {
        if (digits_string.length() < series_length){
            throw std::domain_error("Not enough digits to slice");
        };


        std::vector<std::vector<int>> result_vector;

        // loop through each and every item in the digits_string
        for (int i=0; i<=digits_string.length() - series_length; i++){

            // get the substring in question
            std::string substring;
            substring = digits_string.substr(i, series_length);

            // converte each char from the substring into an int, and append it onto the current_vector container
            std::vector<int> current_vector;
            for (int k=0; k<substring.length(); k++){
                current_vector.push_back(substring.at(k) - '0');
            };

            // as long as the current_vector size matches the desired series length, then we add it to
            // the result
            if (current_vector.size() == series_length){
                result_vector.push_back(current_vector);
            };
        };

        return result_vector;

    };
};