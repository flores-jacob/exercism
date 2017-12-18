#include <string>
#include <iostream>
namespace say
{
    std::string in_english(unsigned long long input)
    {
        std::string ones;
        std::cout << input << std::endl;
        switch(input)
        {
            case 0ULL: ones = "zero"; break;
            case 1ULL: ones = "one"; break;
            case 2ULL: ones = "two"; break;
            case 3ULL: ones = "three"; break;
            case 4ULL: ones = "four"; break;
            case 5ULL: ones = "five"; break;
            case 6ULL: ones = "six"; break;
            case 7ULL: ones = "seven"; break;
            case 8ULL: ones = "eight"; break;
            case 9ULL: ones = "nine"; break;
        };

        return ones;
    };
};