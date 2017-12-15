#include <iostream>
#include <string>
#include <cctype>

namespace bob{
    std::string hey(std::string input_string)
    {   
        // trim whitespace
        while ((input_string.length() != 0) && (input_string.at(input_string.length() - 1) == ' ')){
            input_string = input_string.erase(input_string.length() - 1);
        };
        // check if string is empty
        if (input_string.length() == 0){
            return "Fine. Be that way!";
        };

        // identify the end character
        char end_char = input_string.at(input_string.length() - 1);

        // initialize variables we intend to use to check sentence type
        bool sentence_has_lower_case = false;
        bool sentence_has_alpha = false;

        // check if at least one of the characters is in lower case
        for (int i=0; i<input_string.length(); i++){
            if (islower(input_string.at(i))){
                sentence_has_lower_case = true;            
                break;
            };
        };

        // check if at least one of the characters is part of the alphabet
        for (int i=0; i<input_string.length(); i++){
            if (std::isalpha(input_string.at(i))){
                sentence_has_alpha = true;            
                break;
            };
        };

        if (!sentence_has_lower_case && sentence_has_alpha){
            return "Whoa, chill out!";
        }else if (end_char =='?'){
            return "Sure.";
        };

        return "Whatever.";
    };
}
