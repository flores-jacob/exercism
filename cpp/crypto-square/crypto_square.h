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
            std::vector<std::string> segmented_text;
            std::string cipher_text_result;
            std::string normalized_cipher_text_result;
        public:
            cipher(std::string string_input);
            std::string normalize_plain_text();
            std::vector<std::string> plain_text_segments();
            std::string cipher_text();
            std::string normalized_cipher_text();
    };

    cipher::cipher(std::string string_input)
    {
        input = string_input;
        normalized_input = normalize_plain_text();
        segmented_text = plain_text_segments();
        cipher_text_result = cipher_text();
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

    std::string cipher::cipher_text()
    {
        // if there is no segmented text, return an empty string;
        if (segmented_text.empty()){
            return "";
        };

        // initialize output variable
        std::string cipher_text_result;

        // get the first segment, column length is equal to the length of this first segment
        int n_cols = segmented_text[0].length();
        int n_rows = segmented_text.size();

        // loop through each column element of each segment
        for (int i=0; i<n_cols; i++){
            for (std::string elem: segmented_text){
                if (i < elem.length()){
                    cipher_text_result += elem.at(i);
                };
            };
        };

        return cipher_text_result;
    };

    std::string cipher::normalized_cipher_text()
    {
        if (segmented_text.empty()){
            return "";
        };

        std::string normalized_cipher_text_result;

        // get the number of cols and rows of the segmented text
        int n_cols = segmented_text[0].length();
        int n_rows = segmented_text.size();

        // loop through each row and column
        for (int col=0; col<n_cols; col++){
            for (int row=0; row<n_rows; row++){
                std::string row_element = segmented_text[row];
                // if the current element is not as long as the designated row length,
                // then we pad it with a space
                if (row_element.length() <= col){
                    normalized_cipher_text_result += " ";
                // otherwise, its business as usual, and we append the element on it to the result
                }else{
                    normalized_cipher_text_result += row_element.at(col);
                };
            };

            // once we are done looping through the row items in the column, we append a space
            // as long as this is not the final column
            if (col < n_cols - 1){
                normalized_cipher_text_result += " ";
            };
        };

        return normalized_cipher_text_result;
    };
};