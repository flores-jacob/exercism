#include <string>
#include <iostream>
#include <algorithm>

namespace pangram
{
    bool is_pangram(std::string input){
        //remove all spaces in the input
//        input.erase (std::remove (input.begin(), input.end(), ' '), input.end());

        // if the input does not contain any characters, return 0
        if (input.length() == 0){
            return false;
        };

        std::string alphabet_list = "abcdefghijklmnopqrstuvwxyz";

        for (char letter: alphabet_list){
            std::cout << input << std::endl;
            std::cout << letter << ": " << (std::count(input.begin(), input.end(), letter)) << std::endl;

            if (std::count(input.begin(), input.end(), letter) == 0){
                return false;
            };
        };

        return true;
    };
};