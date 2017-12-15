#include <vector>
#include <map>
// #include <iostream>
#include <locale>
namespace etl 
{
    std::map<char, int> transform(std::map<int, std::vector<char>> old)
    {
        // initialize variables. I'm not sure if initalizing all the variables at the top of the function is good practice or not
        std::vector<char> letter_vector;
        int score;
        std::map<char, int> result;
        // for naming, I'm not sure if lower_case_letter or letter_lower_case would be better. or maybe even lc_letter or letter_lc?
        char lower_case_letter;

        // iterate through each input element (as elem) in the map
        for (auto elem : old){
            // assign the first part of elem as the score
            score = elem.first;
            // assign the second part of elem as the object that holds several characters
            letter_vector = elem.second;

            // iterate through the letter_vector to go through each character
            for (char letter : letter_vector){
                // convert the character to lowercase
                lower_case_letter = std::tolower(letter);
                // std::cout << lower_case_letter << " : " << score <<"\n";
                // insert the pair onto the result vector which we will return afterwards
                result.insert({lower_case_letter, score});
            };
        };
        return result;
    };
};
