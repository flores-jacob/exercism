#include <iostream>

namespace leap {

bool is_leap_year(int int_year)
    {
        // std::cout<<"checking if "<< int_year <<" is a leap year\n";

        // not that readable, but it's in a single line
        return (int_year % 4 == 0) && (!(int_year % 100 == 0) || (int_year % 400 == 0));
    };
};

