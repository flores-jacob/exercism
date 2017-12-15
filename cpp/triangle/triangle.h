#include <string>
#include <stdexcept>
namespace triangle
{

    std::string equilateral = "equilateral";
    std::string isosceles = "isosceles";
    std::string scalene = "scalene";

    std::string kind(float side1, float side2, float side3)
    {
        if ((side1 <= 0) || (side2 <= 0) || (side3 <= 0)){
            throw std::domain_error("sides should not be zero nor negative");
        };

        if (!((side1 + side2) >= side3) || !((side1 + side3) >= side2) || !((side2 + side3) >= side1)){
            throw std::domain_error("not a triangle");
        };


        if ((side1 == side2) && (side2 == side3)){
            return equilateral;
        }else if(
                    (side1 == side2) || (side1 == side3) || (side2 == side3)
                )
        {
            return isosceles;
        }else if((side1 != side2) && (side1 != side3) && (side2 != side3) ){
            return scalene;
        };

    };
};

