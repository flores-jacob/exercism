#include <string>
namespace roman
{
    std::string convert(int input)
    {
        std::string output_roman_numeral;

        int thousands = input / 1000;
        int hundreds = (input - (thousands * 1000)) /100;
        int tens = (input - (thousands * 1000) - (hundreds * 100))/ 10;
        int ones = input - (thousands * 1000) - (hundreds * 100) - (tens * 10);

        std::string thousands_portion(thousands, 'M');
        std::string hundreds_portion;

        switch(hundreds){
            case 1: hundreds_portion = "C"; break;
            case 2: hundreds_portion = "CC"; break;
            case 3: hundreds_portion = "CCC"; break;
            case 4: hundreds_portion = "CD"; break;
            case 5: hundreds_portion = "D"; break;
            case 6: hundreds_portion = "DC"; break;
            case 7: hundreds_portion = "DCC"; break;
            case 8: hundreds_portion = "DCCC"; break;
            case 9: hundreds_portion = "CM"; break;
        };

        std::string tens_portion;

        switch(tens){
            case 1: tens_portion = "X"; break;
            case 2: tens_portion = "XX"; break;
            case 3: tens_portion = "XXX"; break;
            case 4: tens_portion = "XL"; break;
            case 5: tens_portion = "L"; break;
            case 6: tens_portion = "LX"; break;
            case 7: tens_portion = "LXX"; break;
            case 8: tens_portion = "LXXX"; break;
            case 9: tens_portion = "XC"; break;
        };

        std::string ones_portion;

        switch(ones){
            case 1: ones_portion = "I"; break;
            case 2: ones_portion = "II"; break;
            case 3: ones_portion = "III"; break;
            case 4: ones_portion = "IV"; break;
            case 5: ones_portion = "V"; break;
            case 6: ones_portion = "VI"; break;
            case 7: ones_portion = "VII"; break;
            case 8: ones_portion = "VIII"; break;
            case 9: ones_portion = "IX"; break;
        };

        return thousands_portion + hundreds_portion + tens_portion + ones_portion;
    };
};
