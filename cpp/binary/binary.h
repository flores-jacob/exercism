#include <string>
#include <cmath>

namespace binary {
	int convert(std::string input){
        int place_value = 1;
        int decimal_value = 0;
        for (int i=input.length() - 1; i >=0 ; i--, place_value <<= 1){
            char current_char = input.at(i);
            // if the current char is neither a 0 or a 1, break and just return 0
            if ((current_char != '0') && (current_char != '1')){
                break;
            };
            // casting char to int value https://stackoverflow.com/a/30727561
            int current_int = current_char - '0';
            decimal_value += current_int * place_value;
		};
		return decimal_value;
	};
};
