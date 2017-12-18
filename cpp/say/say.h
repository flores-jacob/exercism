#include <string>
#include <iostream>
namespace say
{
    std::string in_english(unsigned long long input)
    {
        int tens_ones_input = input;
        int tens_input = tens_ones_input/10;
        int ones_input = (input - (tens_input * 10));

        std::string tens_ones_string;

        if (tens_ones_input < 20)
        {
            std::string teens;
            switch(tens_ones_input)
            {
                case 0: tens_ones_string = "zero"; break;
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

            std::string ones;
            std::cout << "ones input: " << ones_input << std::endl;
            switch(ones_input)
            {
                case 0: ones = ""; break;
                case 1: ones = "one"; break;
                case 2: ones = "two"; break;
                case 3: ones = "three"; break;
                case 4: ones = "four"; break;
                case 5: ones = "five"; break;
                case 6: ones = "six"; break;
                case 7: ones = "seven"; break;
                case 8: ones = "eight"; break;
                case 9: ones = "nine"; break;
            };

            if (ones_input ==  0){
                tens_ones_string = tens;
            }else{
                tens_ones_string = tens + "-" + ones;
            };


        };

        std::cout << "tens ones string: " << tens_ones_string << std::endl;
        return tens_ones_string;
    };
};