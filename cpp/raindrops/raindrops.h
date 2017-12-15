#include <string>

namespace raindrops
{
    std::string convert(int input)
    {
        std::string constructed_string;

        if (input % 3 == 0){ constructed_string += "Pling"; };
        if (input % 5 == 0){ constructed_string += "Plang"; };
        if (input % 7 == 0){ constructed_string += "Plong"; };

        if (constructed_string.empty()){
            constructed_string = std::to_string(input);
        };

        return constructed_string;
    };
};
