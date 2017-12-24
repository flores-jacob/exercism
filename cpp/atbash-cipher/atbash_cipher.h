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

                if (counter % 5 == 0 && output_string.length() < input_lower_case.length()){
                    output_string += " ";
                };
                counter += 1;
            };
        };

        return output_string;
    };

    std::string decode(std::string input_string){
        // remove spaces
        input_string.erase (std::remove (input_string.begin(), input_string.end(), ' '), input_string.end());


        std::string output_string;

        for (char elem: input_string){
            int pos = cipher_text.find(elem);
            output_string += plain_text.at(pos);
        };

        return output_string;
    };
};
