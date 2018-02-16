#include <string>
#include <cmath>

namespace binary {
	int convert(std::string input){
        int place_value = 1;
        int decimal_value = 0;
        for (int i=input.length() - 1; i >=0 ; i--, place_value <<= 1){
            char current_char = input.at(i);
            if (current_char == '1')
            {
                decimal_value += place_value;
            }
            else if (current_char != '0')
            {
                return 0;
            }
        };
		return decimal_value;
	};
};
