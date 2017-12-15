#include <string>
#include <locale>
#include <vector>
#include <cmath>
#include <iostream>

namespace crypto_square
{
    class cipher{
        private:
            std::string input;
            std::string normalized_input;
        public:
            cipher(std::string string_input);
            std::string normalize_plain_text();
            std::vector<std::string> plain_text_segments();
    };

    cipher::cipher(std::string string_input)
    {
        input = string_input;
        normalized_input = normalize_plain_text();
    };

    std::string cipher::normalize_plain_text()
    {

        std::string normalized_text;
        // keep only alphanumeric characters and convert to lower case
        for (char elem: input){
            if (isalnum(elem))
            {
                normalized_text += std::tolower(elem);
            };
        };

        return normalized_text;
    };

    std::vector<std::string> cipher::plain_text_segments()
    {
        // if the string is empty, return an empty vector
        if (normalized_input.empty()){
            return {};
        };

        // initialize output variable
        std::vector<std::string> text_segments_vector;

        // compute what value to use for rows and columns
        int n_rows = std::sqrt(normalized_input.length());

        int n_cols;
        if (normalized_input.length() % n_rows !=0){
            n_cols = n_rows + 1;
        }else{
            n_cols = n_rows;
        };

        // loop through each character in the input string
        std::string current_segment;
        for (int i=0; i<normalized_input.length(); i++)
        {
            // append the current character to the segment we are forming
            current_segment += normalized_input.at(i);

            // if the segment is now as long as the desired number of rows, we append the result
            // to the output variable, and move on to the next segment
            if (current_segment.length() == n_cols){
                text_segments_vector.push_back(current_segment);
                current_segment = "";
            };
            // if we have reached the end of the string, and there is still an unappended segment
            // to the result, we append it
            if (((i + 1) == normalized_input.length()) && (!current_segment.empty())){
                text_segments_vector.push_back(current_segment);
            };
        };

        return text_segments_vector;
    };

};