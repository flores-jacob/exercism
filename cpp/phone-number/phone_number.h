#include <string>
#include <locale>
#include <iostream>


class phone_number
{
    private:
        std::string parsed_number;
    public:
        phone_number(std::string preprocessed_phone_number);
        std::string number() const;
        std::string area_code() const;
        operator std::string() const;
};

phone_number::phone_number(std::string preprocessed_phone_number)
{
    // loop through input, and only retain the digits
    for (char number: preprocessed_phone_number){
        if (std::isdigit(number)){
            parsed_number += number;
        };
    };
    
    // check number length. if length is 11, and number begins with country code 1, then return last 10 numbers
    if ((parsed_number.length() == 11) && (parsed_number.at(0) == '1')){
        parsed_number = parsed_number.substr(1);
    // if country code is not 1, return 0000000000
    }else if ((parsed_number.length() == 11) && (parsed_number.at(0) != '1')){
        parsed_number = "0000000000";
    // append 1 in the beginning of the area code if number is 9 digits
    }else if (parsed_number.length() < 10){
        parsed_number = "0000000000";
    };

};

// return the unformatted number
std::string phone_number::number() const
{
    return parsed_number;
};
// return the area code
std::string phone_number::area_code() const
{
    return parsed_number.substr(0,3);
};
// return the formatted number if cast into the std::string type
phone_number::operator std::string() const
{
    return "(" + parsed_number.substr(0,3) + ") " + parsed_number.substr(3,3) + "-" + parsed_number.substr(6);
};

