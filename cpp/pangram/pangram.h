#include <string>
#include <algorithm>
#include <locale>

namespace pangram
{
    bool is_pangram(std::string input){
        // if the input does not contain any characters, return 0
        if (input.length() == 0){
            return false;
        };

        // convert input to lowercase
        std::string input_lower_case;

        // convert the input string to lower case
        for (char elem: input){
            input_lower_case += std::tolower(elem);
        };
        
        std::string alphabet_list = "abcdefghijklmnopqrstuvwxyz";

        for (char letter: alphabet_list){
            if (std::count(input_lower_case.begin(), input_lower_case.end(), letter) == 0){
                return false;
            };
        };

        return true;
    };
};