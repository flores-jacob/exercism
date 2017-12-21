#include <string>

namespace date_independent
{
    class clock
    {
        private:
            int hour;
            int minute;
        public:
            clock();
            static std::string at(int hour_in, int minute_in);
    };

    clock::clock()
    {
        hour = 0;
        minute = 0;
    };

    std::string clock::at(int hour_in, int minute_in)
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

        // we combine the strings and return them
        return hour_string + ":" + minute_string;
    };

};