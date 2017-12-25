#include <string>

namespace pangram
{
    bool is_pangram(std::string input){
        if (input.length() == 0){
            return false;
        };
    };
};