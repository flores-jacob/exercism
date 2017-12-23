#include <string>
#include <cmath>
#include <set>

namespace hexadecimal {
	int convert(std::string input){
		int decimal_value = 0;
		for (int i=input.length() - 1; i >=0 ; i--){
			char current_char = input.at(i);

            // initialize int variable
            int current_int;

            // check if char is from a to f (which represents 10 to 16)
            // then convert value to decimal by subtracting 87
            std::set<char> hexcharset{'a', 'b', 'c', 'd', 'e', 'f'};
            std::set<char> hexcharintset{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

            if (hexcharset.count(current_char) == 1){
                current_int = current_char - 87;
            // if it's not, it's probably an int
            }else if (hexcharintset.count(current_char) == 1){
			    current_int = current_char - '0';
            }else{
                return 0;
            };

			// casting char to int value https://stackoverflow.com/a/30727561
			int place_value = std::pow(16, abs((i  + 1) - input.length()));
			decimal_value += current_int * place_value;
		};
		return decimal_value;
	};
};
