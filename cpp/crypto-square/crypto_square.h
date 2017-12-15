#include <string>
#include <algorithm>
#include <locale>
namespace crypto_square
{
    class cipher{
        private:
            std::string input;
        public:
            cipher(std::string string_input);
            std::string normalize_plain_text();
    };

    cipher::cipher(std::string string_input)
    {
        input = string_input;
    };

    std::string cipher::normalize_plain_text()
    {
        std::string normalized_text;


        // convert to lower case
        for (char elem: input){
            normalized_text += std::tolower(elem);
        };

        // remove whitespace https://stackoverflow.com/a/83538
        normalized_text.erase(std::remove_if(normalized_text.begin(), normalized_text.end(), isspace), normalized_text.end());

        // remove whitespace https://stackoverflow.com/a/83481 (first comment)
        // normalized_text.erase (std::remove (normalized_text.begin(), normalized_text.end(), ' '), normalized_text.end());

        return normalized_text;
    };
};