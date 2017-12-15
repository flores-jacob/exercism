#include <map>
#include <string>
#include <vector>
#include <algorithm>

namespace word_count
{
    std::map<std::string, int> words(std::string input_string)
    {
        std::vector<std::string> intermediate_string_vector;
        std::string intermediate_word;

        // Examine the string character by character
        for (char character : input_string){
            // if we encounter any of these delimiters, we end the current word          
            if ((character == ' ') || (character == '\n') || (character == ',')){
                // move on to next word, append word to list
                intermediate_string_vector.push_back(intermediate_word);
                // "reset" the current intermediate word to zero
                intermediate_word = "";
            } else {
                // append character to word we are forming
                intermediate_word += character;
            };
        };

        // once done, insert the final word onto a list we will process further
        intermediate_string_vector.push_back(intermediate_word);
        

        // Now we have split the string using spaces. Our next task is to clean up each word to remove leading and trailing non alphanumeric characters
        // we loop through each string in the list of strings (intermediate_string_vector)
        for (int i=0; i<intermediate_string_vector.size(); i++){
            // assign current_string as the string we will be working on in this iteration
            std::string current_string = intermediate_string_vector.at(i);
            
            // trim leading non alphanumeric chars in the current string
            // as long as the string is not empty, and its first character is not alphanumeric, erase the first character
            while (!current_string.empty() && (!std::isalnum(current_string.at(0)))){
                // current_string.erase(0) does not work. Why?
                current_string.erase(current_string.begin());
            };
                        
            // trim trailing non-alphanumeric chars
            // as long as the string is not empty, and its last character is not alphanumeric, erase the last character
            while (!current_string.empty() && (!std::isalnum(current_string.at(current_string.length() -1)))){
                current_string.erase(current_string.length() -1);
            };            
          
            // we should now have a string that only begins and ends with alphanumeric characters, so we can now proceed to process it further
            
            // convert the string to lower case
            std::transform(current_string.begin(), current_string.end(), current_string.begin(), ::tolower);
            // update the value of the string in the vector, with the cleaned up version
            intermediate_string_vector[i] = current_string;
        };


        // now, we prepare the final result

        // initialize the final value we will be returning
        std::map<std::string, int> final_result;

        // now we loop through the vector so that we can count the occurences of each string
        for (auto elem: intermediate_string_vector){
            // make sure we only deal with non-empty strings
            if (!elem.empty()){
                // count
                int count_identical = std::count(intermediate_string_vector.begin(),  intermediate_string_vector.end(), elem);
                // assign the value into the preclared final map
                final_result[elem] = count_identical;
            };
        };
        
        return final_result;
    };
};

// Notes:
/*
1. I tried to check if there's a simple way to split a string using a given delimiter. Unfortunately, most answers I found had to include a lot of items (sometimes more than 5) for their solutions to work.  Some of the solutions even requried the inclusion of boost functionality. I would like to avoid this, since boost may not always be present in all projects. Some solutions also advised to use strtok (a C library it seems) but a lot of people are also averse to this. In the end, I had to cook up a solution of my own.  However, whether or not this will hold up when dealing with different types of encodings (asii, utf-8, utf-16, etc) remains to be seen.

helpful tutorial https://www.fluentcpp.com/2017/04/21/how-to-split-a-string-in-c/
*/
