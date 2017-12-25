#include <string>
#include <algorithm>

namespace pangram
{
    bool is_pangram(std::string input){
        if (input.length() == 0){
            return false;
        };

        std::string alphabet_list = "abcdefghijklmnopqrstuvwxyz";

        for (char letter: alphabet_list){
            if (std::count(input.begin(), input.end(), letter) != 1){
                return false;
            };
        };

        return true;

    };
};