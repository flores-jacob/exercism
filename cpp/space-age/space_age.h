#include <math.h>
#include <iostream>
#include <limits>
namespace space_age{
    class space_age{
        private:
            float age_in_seconds;
            float age_on_earth;
            float age_on_mercury;
            float age_on_venus;
            float age_on_mars;
            float age_on_jupiter;
            float age_on_saturn;
            float age_on_uranus;
            float age_on_neptune;
            const float seconds_in_earth_year = 31557600.0;
        public:
            space_age(float age_in_seconds_input);
            float seconds() const;
            float on_earth() const;
            float on_mercury() const;
            float on_venus() const;
            float on_mars() const;
            float on_jupiter() const;
            float on_saturn() const;
            float on_uranus() const;
            float on_neptune() const;
    };

    space_age::space_age(float age_in_seconds_input)
    {
        age_in_seconds = age_in_seconds_input;

        age_on_earth = roundf((age_in_seconds/seconds_in_earth_year) * 100)/100;
        age_on_mercury = roundf(((age_in_seconds/seconds_in_earth_year)/0.2408467) * 100)/100;
        age_on_venus = roundf(((age_in_seconds/seconds_in_earth_year)/0.61519726) * 100)/100;
        age_on_mars = roundf(((age_in_seconds/seconds_in_earth_year)/1.8808158) * 100)/100;    
        age_on_jupiter = roundf(((age_in_seconds/seconds_in_earth_year)/11.862615) * 100)/100;
        age_on_saturn = roundf(((age_in_seconds/seconds_in_earth_year)/29.447498) * 100)/100;
        age_on_uranus = roundf(((age_in_seconds/seconds_in_earth_year)/84.016846) * 100)/100;
        age_on_neptune = roundf(((age_in_seconds/seconds_in_earth_year)/164.79132) * 100)/100;

    };

    float space_age::seconds() const
    {
        return age_in_seconds;
    };

    float space_age::on_earth() const
    {

        return age_on_earth;
    };

    float space_age::on_mercury() const
    {
        return age_on_mercury;
    };

    float space_age::on_venus() const
    {
        return age_on_venus;
    };

    float space_age::on_mars() const
    {
        return age_on_mars;
    };

    float space_age::on_jupiter() const
    {
        return age_on_jupiter;
    };

    float space_age::on_saturn() const
    {
        return age_on_saturn;
    };

    float space_age::on_uranus() const
    {
        return age_on_uranus;
    };

    float space_age::on_neptune() const
    {
        return age_on_neptune;
    };

};



