#include <string>
#include <vector>

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
        std::vector<std::vector<int>> result_vector;

        // loop through each and every item in the digits_string
        for (int i=0; i<=digits_string.length() - series_length; i++){
            std::vector<int> current_vector;
            // loop through each succeeding digit up to the indicated series_length
            for (int k=0; k < series_length; k++){
                // continue looping as long as we do not exceed the length of the original digits_string
                if (k + i <= digits_string.length()){
                    // convert each char into an int, and add it to the current_vector we are building
                    current_vector.push_back(digits_string.at(i+k) - 48);
                // if we have exceeded the length of the original digits_string, then we break the for loop
                }else{
                    break;
                };

                // as long as the current_vector size matches the desired series length, then we add it to
                // the result
                if (current_vector.size() == series_length){
                    result_vector.push_back(current_vector);
                };
            };
        };

        return result_vector;

    };
};