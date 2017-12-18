#include <string>
#include <cmath>

namespace trinary {
	int to_decimal(std::string input){
		int decimal_value = 0;
		for (int i=input.length() - 1; i >=0 ; i--){
			char current_char = input.at(i);
			// if the current char is neither a 0, 1, or 2, break and just return 0
			if ((current_char != '0') && (current_char != '1') && (current_char != '2')){
				return 0;
			};
			// casting char to int value https://stackoverflow.com/a/30727561
			int current_int = current_char - 48;
			int place_value = std::pow(3, abs((i  + 1) - input.length()));
			decimal_value += current_int * place_value;
		};
		return decimal_value;
	};
};
