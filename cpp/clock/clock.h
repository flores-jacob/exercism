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
        return std::to_string(hour_in) + ":" + std::to_string(minute_in);
    };

};