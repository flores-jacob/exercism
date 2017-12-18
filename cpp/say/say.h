#include <string>
#include <iostream>
#include <vector>

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

    std::string hundreds_chunk_parser(int input)
    {

        int hundreds_input = input /100;
        int tens_ones_input = input - (hundreds_input * 100);
        int tens_input = (input - (hundreds_input * 100))/10;
        int ones_input = (input - (hundreds_input * 100) - (tens_input * 10));

        std::cout << "hundreds input: " << input << std::endl;
        std::cout << "tens_ones_input " << tens_ones_input << std::endl;
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

//        std::vector<std::string> string_vector = {hundreds_string, tens_ones_string};
//
        std::string compound_string;
//        for (int i=string_vector.size() - 1; i >= 0; i--){
//            if (string_vector.at(i) != ""){
//                compound_string = string_vector.at(i) + " " + compound_string;
//            };
//        };

        if ((tens_ones_string != "") && (hundreds_string !="")){
            compound_string = hundreds_string + " " + tens_ones_string;
        }else if((tens_ones_string == "") && (hundreds_string !="")){
            compound_string = hundreds_string;
        }else if((tens_ones_string != "") && (hundreds_string =="")){
            compound_string = tens_ones_string;
        };

        return compound_string;

    };

    std::string in_english(unsigned long long input)
    {

        if (input == 0ULL){
            return "zero";
        };

        int billions_input = input/1000000000;
        int millions_input = (input - (billions_input * 1000000000))/1000000;
        std::cout << "millions " << millions_input << std::endl;

        int thousands_input = (input - (billions_input * 1000000000) - (millions_input * 1000000))/1000;
        int hundreds_tens_ones_input = (input - (billions_input * 1000000000) - (millions_input * 1000000) - (thousands_input * 1000));

        std::string hundreds_string = hundreds_chunk_parser(hundreds_tens_ones_input);

        std::string thousands_string;
        if (thousands_input > 0){
            thousands_string = hundreds_chunk_parser(thousands_input) + " thousand";
        }else{
            thousands_string = "";
        };

        std::string millions_string;
        if (millions_input > 0){
            millions_string = hundreds_chunk_parser(millions_input) + " million";
        }else{
            millions_string = "";
        };

        std::string billions_string;
        if (billions_input > 0){
            billions_string = hundreds_chunk_parser(billions_input) + " billion";
        }else{
            billions_string = "";
        };

        std::string compound_string;
        std::vector<std::string> numbers_vector = {billions_string, millions_string, thousands_string, hundreds_string};

        for (std::string elem: numbers_vector){
            if (!elem.empty()){
                compound_string += elem + " ";
            };
        };


        // trim whitespace at the end
        while ((compound_string.length() != 0) && (compound_string.at(compound_string.length() - 1) == ' ')){
            compound_string = compound_string.erase(compound_string.length() - 1);
        };

        return compound_string;
    };
};
