#include <string>
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
        // keep only alphanumeric characters and convert to lower case
        for (char elem: input){
            if (isalnum(elem))
            {
                normalized_text += std::tolower(elem);
            };
        };

        return normalized_text;
    };
};