#include <string>

namespace atbash
{
    std::string plain_text = "abcdefghijklmnopqrstuvwxyz";
    std::string cipher_text = "zyxwvutsrqponmlkjihgfedcba";

    std::string encode(std::string input_string)
    {
        std::string output_string;

        for (char elem:input_string){
            int pos = plain_text.find(elem);
            output_string += cipher_text.at(pos);
        };

        return output_string;
    };
};