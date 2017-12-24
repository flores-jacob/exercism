#include <string>
#include <algorithm>
#include <locale>
namespace atbash
{
    std::string plain_text = "abcdefghijklmnopqrstuvwxyz1234567890";
    std::string cipher_text = "zyxwvutsrqponmlkjihgfedcba1234567890";

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
        int counter = 1;

        for (char elem: input_lower_case){
            if (std::isalnum(elem)){
                int pos = plain_text.find(elem);
                output_string += cipher_text.at(pos);

                if (counter % 5 == 0){
                    output_string += " ";
                };
                counter += 1;
            };
        };

        return output_string;
    };
};