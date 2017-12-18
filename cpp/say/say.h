#include <string>
#include <iostream>
namespace say
{

    std::string unit_value(int unit_value_input)
    {
        std::string unit_value;
        switch(unit_value_input)
        {
            case 0: unit_value = ""; break;
            case 1: unit_value = "one"; break;
            case 2: unit_value = "two"; break;
            case 3: unit_value = "three"; break;
            case 4: unit_value = "four"; break;
            case 5: unit_value = "five"; break;
            case 6: unit_value = "six"; break;
            case 7: unit_value = "seven"; break;
            case 8: unit_value = "eight"; break;
            case 9: unit_value = "nine"; break;
        };

        return unit_value;
    };

    std::string in_english(unsigned long long input)
    {

        if (input == 0ULL){
            return "zero";
        };

        int hundreds_input = input/100;
        int tens_ones_input = input - (hundreds_input * 100);
        int tens_input = tens_ones_input/10;
        int ones_input = (input - (hundreds_input * 100) - (tens_input * 10));

        std::string tens_ones_string;
        std::string final_string;

        if (tens_ones_input < 20)
        {
            std::string teens;
            switch(tens_ones_input)
            {
                // case 0: tens_ones_string = "zero"; break;
                case 1: tens_ones_string = "one"; break;
                case 2: tens_ones_string = "two"; break;
                case 3: tens_ones_string = "three"; break;
                case 4: tens_ones_string = "four"; break;
                case 5: tens_ones_string = "five"; break;
                case 6: tens_ones_string = "six"; break;
                case 7: tens_ones_string = "seven"; break;
                case 8: tens_ones_string = "eight"; break;
                case 9: tens_ones_string = "nine"; break;
                case 10: tens_ones_string = "ten"; break;
                case 11: tens_ones_string = "eleven"; break;
                case 12: tens_ones_string = "twelve"; break;
                case 13: tens_ones_string = "thirteen"; break;
                case 14: tens_ones_string = "fourteen"; break;
                case 15: tens_ones_string = "fifteen"; break;
                case 16: tens_ones_string = "sixteen"; break;
                case 17: tens_ones_string = "seventeen"; break;
                case 18: tens_ones_string = "eighteen"; break;
                case 19: tens_ones_string = "nineteen"; break;
            };

        }else

        {
            std::string ones = unit_value(ones_input);
            std::cout << "ones input: " << ones_input << std::endl;

            std::string tens;
            std::cout << "tens input: " << tens_input << std::endl;
            switch(tens_input)
            {
                case 0: tens = ""; break;
                case 1: tens = "ten"; break;
                case 2: tens = "twenty"; break;
                case 3: tens = "thirty"; break;
                case 4: tens = "forty"; break;
                case 5: tens = "fifty"; break;
                case 6: tens = "sixty"; break;
                case 7: tens = "seventy"; break;
                case 8: tens = "eighty"; break;
                case 9: tens = "ninety"; break;
            };

            if (ones_input ==  0){
                tens_ones_string = tens;
            }else if (tens_input == 0){
                tens_ones_string = "";
            }else{
                tens_ones_string = tens + "-" + ones;
            };
        };

        std::string hundreds_string;
        if (hundreds_input > 0){
            hundreds_string = unit_value(hundreds_input) + " hundred";
        }else{
            hundreds_string = "";
        };

        std::cout << "hundreds input: " << hundreds_input << std::endl;

        if ((hundreds_string != "") && (tens_ones_string != "")){
            final_string = hundreds_string + " " + tens_ones_string;
        }else if (tens_ones_string != ""){
            final_string = tens_ones_string;
        }else{
            final_string = hundreds_string;
        };

        return final_string;
    };
};