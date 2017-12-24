#include <string>
#include <algorithm>
namespace atbash
{
    std::string plain_text = "abcdefghijklmnopqrstuvwxyz";
    std::string cipher_text = "zyxwvutsrqponmlkjihgfedcba";

    std::string encode(std::string input_string)
    {
        std::string input_lower_case;

        // convert the input string to lower case
        for (char elem: input_string){
            input_lower_case += std::tolower(elem);
        };

        // remove spaces
        input_lower_case.erase (std::remove (input_lower_case.begin(), input_lower_case.end(), ' '), input_lower_case.end());

        std::string output_string;

        for (char elem: input_lower_case){
            int pos = plain_text.find(elem);
            output_string += cipher_text.at(pos);
        };

        return output_string;
    };
};