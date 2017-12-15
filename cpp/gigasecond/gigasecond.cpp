// #include <iostream>
#include "gigasecond.h"

namespace gigasecond{
    boost::posix_time::ptime advance(boost::posix_time::ptime input_time){
        // std::cout << input_time << std::endl;
        
        return input_time + boost::posix_time::seconds(1000000000);
    }
};
