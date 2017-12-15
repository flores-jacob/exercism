#include <string>
#include <vector>
#include <iostream>
#include <locale>

namespace anagram{
    class anagram
    {
        private:
            std::string string_input;
            int input_length;

        public:
            anagram(std::string str_in);
            // How to use "auto" https://stackoverflow.com/a/44801859 
            auto matches(std::vector<std::string> str_list_in) -> std::vector<std::string>;
    };

    anagram::anagram(std::string str_in)
    {   
        string_input = str_in;
        input_length = str_in.length();

    };

    // How to initialize a list of strings https://stackoverflow.com/q/44340589
    auto anagram::matches(std::vector<std::string> str_list_in) -> std::vector<std::string>
    {
        // std::cout << "processing new set for " << string_input << "\n";
        std::vector<std::string> str_list_out;

        int input_letter_count;
        int comparison_letter_count;

        for (int i=0; i<str_list_in.size(); i++){
            // std::cout << " " << "comparing " << str_list_in.at(i) << "\n";
            // check if words are of the same length, if they're not, move on to the next word
            if (str_list_in.at(i).length() != input_length){
            // std::cout << "   " <<"different lengths " << "\n";
                continue;
            };



            // check if the word is being compared to itself, if it is move on to the next word
            std::string input_lower_case;
            std::string comp_lower_case;

            // convert the input string to lower case
            for (char elem: string_input){
                input_lower_case += std::tolower(elem);
            };

            // compare the comp string to lower case
            for (char elem: str_list_in.at(i)){
                comp_lower_case += std::tolower(elem);
            };

            // if both strings are identical, move on the the next word
            if (input_lower_case == comp_lower_case){
                continue;
            };


            // check if each letter has the same count
            // loop through each letter of the string_input variable
            for (int j=0; j<string_input.length(); j++){
                // std::cout << "     " <<"input letter " << string_input.at(j) << "\n";
                // start the count from zero
                input_letter_count = 0;
                comparison_letter_count = 0;
                // compare the current letter with all of the other letters in the string_input variable
                // add +1 to the count if there's a match
                for (int k=0; k<string_input.length(); k++){
                    // std::cout << "     " <<"compare " << string_input.at(j) << " with input " << string_input.at(k) << "\n";
                    if (string_input.at(k) == string_input.at(j)){
                        input_letter_count = input_letter_count + 1;
                    };
                };

                // std::cout << "     string_input " << string_input.at(j) << " = " << input_letter_count << "\n";

                // compare the current letter with all of the letters in the other word
                for (int k=0; k<str_list_in.at(i).length(); k++){
                    // std::cout << "     " <<"compare " << string_input.at(j) << " with  comp " << str_list_in.at(i).at(k) << "\n";
                    if (str_list_in.at(i).at(k) == string_input.at(j)){
                        comparison_letter_count = comparison_letter_count + 1;
                    };
                };

                // std::cout << "     comp_input   " << string_input.at(j) << " = " << comparison_letter_count << "\n";
            };

            // if the count for a letter type is not the same with the other word's letter type count, then we skip to the next letter
            if (input_letter_count != comparison_letter_count){
                // std::cout << "          " << string_input << " != " << str_list_in.at(i) << "\n";
                continue;
            };

            // if we have successfully compared all letter counts, then we add the word onto the final list
            // std::cout << "SUCCESS match " << string_input << " == " << str_list_in.at(i) << "\n";
            str_list_out.push_back(str_list_in.at(i));

        };
        // std::cout<<"final list: ";
        // for (int i=0; i<str_list_out.size(); i++){
        // std::cout<< str_list_out.at(i) << " ";
        // };

        // std::cout << "\n";
        return str_list_out;
    };
};
