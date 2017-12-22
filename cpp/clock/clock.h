#include <string>

namespace date_independent
{
    class clock
    {
        private:
            int hour;
            int minute;
            std::string hour_string;
            std::string minute_string;
            std::string compound_string;
        public:
            clock();
            // this function is static because the test cases call it without instantiating
            // a clock object
            static clock at(int hour_in, int minute_in);
            clock plus(int additional_minutes);
            operator std::string() const;
            bool operator== (const clock &rhs) const;

    };

    clock::clock()
    {
    };

    clock clock::at(int hour_in, int minute_in)

    {
        // adjust the number of hours by the number of times the minute hand goes around the clock face
        int hour_adjust = minute_in/60;
        // we will only show the minute remainder
        int minute_val = minute_in % 60;

        // if the number of minutes are negative, we get the correct number of minutes by subtracting
        // the negative value from the "whole" value of 60
        if (minute_val < 0){
            minute_val = 60 + minute_val;
            // we also adjust the number of hours by -1
            hour_adjust -= 1;
        };

        // we apply the total hour adjustments
        hour_in += hour_adjust;

        // we get the remainder hours after dividing by 24 hours
        int hour_val = hour_in % 24;

        // if the value of the number of hours is negative, we subtract the value from the "whole" value
        // of 24 hours
        if (hour_val < 0){
            hour_val = 24 + hour_val;
        };

        // we convert the hours and minutes to strings
        std::string hour_string = std::to_string(hour_val);
        std::string minute_string = std::to_string(minute_val);

        // we pad the strings with 0 if the digits are less than 10
        if (hour_val < 10){
            hour_string = "0" + std::to_string(hour_val);
        };

        if (minute_val < 10){
            minute_string = "0" + std::to_string(minute_val);
        };

        // Initialize a new clock object to hold the values
        clock clock_object;

        // assign the integer and string values
        clock_object.minute_string = minute_string;
        clock_object.hour_string = hour_string;
        clock_object.minute = minute_val;
        clock_object.hour = hour_val;
        clock_object.compound_string = hour_string + ":" + minute_string;

        // return the clock object that now has the desired values
        return clock_object;
    };

    clock clock::plus(int additional_minutes){
        return at(hour, minute + additional_minutes);
    };

    clock::operator std::string() const
    {
        return compound_string;
    };

    bool clock::operator == (const clock &rhs) const
    {
        return rhs.compound_string == compound_string;
    };


};