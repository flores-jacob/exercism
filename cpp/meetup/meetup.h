#include <boost/date_time/gregorian/gregorian.hpp>
#include <vector>

namespace meetup
{
    class scheduler
    {
        private:
            int year;
            int month;
            std::vector<int> teenth_list = {13, 14, 15, 16, 17, 18, 19};
            std::vector<int> day_list;
            boost::gregorian::date end_of_month;

        public:
            // https://stackoverflow.com/a/39888153
            scheduler(int month_in, int year_in);

            boost::gregorian::date dayteenth(boost::date_time::weekdays day_of_week) const;

            boost::gregorian::date monteenth() const {return dayteenth(boost::gregorian::Monday);};
            boost::gregorian::date tuesteenth() const {return dayteenth(boost::gregorian::Tuesday);};
            boost::gregorian::date wednesteenth() const {return dayteenth(boost::gregorian::Wednesday);};
            boost::gregorian::date thursteenth() const {return dayteenth(boost::gregorian::Thursday);};
            boost::gregorian::date friteenth() const {return dayteenth(boost::gregorian::Friday);};
            boost::gregorian::date saturteenth() const {return dayteenth(boost::gregorian::Saturday);};
            boost::gregorian::date sunteenth() const {return dayteenth(boost::gregorian::Sunday);};

            boost::gregorian::date nth_weekday(boost::date_time::weekdays day_of_week, int n) const;
            boost::gregorian::date first_monday() const {return nth_weekday(boost::gregorian::Monday, 1);};
            boost::gregorian::date first_tuesday() const {return nth_weekday(boost::gregorian::Tuesday, 1);};
            boost::gregorian::date first_wednesday() const {return nth_weekday(boost::gregorian::Wednesday, 1);};
            boost::gregorian::date first_thursday() const {return nth_weekday(boost::gregorian::Thursday, 1);};
            boost::gregorian::date first_friday() const {return nth_weekday(boost::gregorian::Friday, 1);};
            boost::gregorian::date first_saturday() const {return nth_weekday(boost::gregorian::Saturday, 1);};
            boost::gregorian::date first_sunday() const {return nth_weekday(boost::gregorian::Sunday, 1);};

            boost::gregorian::date second_monday() const {return nth_weekday(boost::gregorian::Monday, 2);};
            boost::gregorian::date second_tuesday() const {return nth_weekday(boost::gregorian::Tuesday, 2);};
            boost::gregorian::date second_wednesday() const {return nth_weekday(boost::gregorian::Wednesday, 2);};
            boost::gregorian::date second_thursday() const {return nth_weekday(boost::gregorian::Thursday, 2);};
            boost::gregorian::date second_friday() const {return nth_weekday(boost::gregorian::Friday, 2);};
            boost::gregorian::date second_saturday() const {return nth_weekday(boost::gregorian::Saturday, 2);};
            boost::gregorian::date second_sunday() const {return nth_weekday(boost::gregorian::Sunday, 2);};

            boost::gregorian::date third_monday() const {return nth_weekday(boost::gregorian::Monday, 3);};
            boost::gregorian::date third_tuesday() const {return nth_weekday(boost::gregorian::Tuesday, 3);};
            boost::gregorian::date third_wednesday() const {return nth_weekday(boost::gregorian::Wednesday, 3);};
            boost::gregorian::date third_thursday() const {return nth_weekday(boost::gregorian::Thursday, 3);};
            boost::gregorian::date third_friday() const {return nth_weekday(boost::gregorian::Friday, 3);};
            boost::gregorian::date third_saturday() const {return nth_weekday(boost::gregorian::Saturday, 3);};
            boost::gregorian::date third_sunday() const {return nth_weekday(boost::gregorian::Sunday, 3);};

            boost::gregorian::date fourth_monday() const {return nth_weekday(boost::gregorian::Monday, 4);};
            boost::gregorian::date fourth_tuesday() const {return nth_weekday(boost::gregorian::Tuesday, 4);};
            boost::gregorian::date fourth_wednesday() const {return nth_weekday(boost::gregorian::Wednesday, 4);};
            boost::gregorian::date fourth_thursday() const {return nth_weekday(boost::gregorian::Thursday, 4);};
            boost::gregorian::date fourth_friday() const {return nth_weekday(boost::gregorian::Friday, 4);};
            boost::gregorian::date fourth_saturday() const {return nth_weekday(boost::gregorian::Saturday, 4);};
            boost::gregorian::date fourth_sunday() const {return nth_weekday(boost::gregorian::Sunday, 4);};

            boost::gregorian::date last_weekday(boost::date_time::weekdays day_of_week) const;
            boost::gregorian::date last_monday() const {return last_weekday(boost::gregorian::Monday);};
            boost::gregorian::date last_tuesday() const {return last_weekday(boost::gregorian::Tuesday);};
            boost::gregorian::date last_wednesday() const {return last_weekday(boost::gregorian::Wednesday);};
            boost::gregorian::date last_thursday() const {return last_weekday(boost::gregorian::Thursday);};
            boost::gregorian::date last_friday() const {return last_weekday(boost::gregorian::Friday);};
            boost::gregorian::date last_saturday() const {return last_weekday(boost::gregorian::Saturday);};
            boost::gregorian::date last_sunday() const {return last_weekday(boost::gregorian::Sunday);};

    };
    
    scheduler::scheduler(int month_in, int year_in): month(month_in), year(year_in)
    {
    	boost::gregorian::date given_date(year, month, 1);
    	end_of_month = given_date.end_of_month();

    	// put the list of days for the month onto the day_list vector
    	for (int i=1; i<=end_of_month.day(); i++){
    		day_list.push_back(i);
    	};
    };


    boost::gregorian::date scheduler::dayteenth(boost::date_time::weekdays day_of_week) const
    {
    	for (auto teenth_day : teenth_list){
            boost::gregorian::date given_date(year, month, teenth_day);
            if (given_date.day_of_week() == day_of_week) {
            	return given_date;
            };
    	};
    };


    boost::gregorian::date scheduler::nth_weekday(boost::date_time::weekdays day_of_week, int n) const
    {
    	int day_count = 0;
    	for (auto day : day_list){
            boost::gregorian::date given_date(year, month, day);
            if (given_date.day_of_week() == day_of_week) {
            	if (day_count==n - 1){
            		return given_date;
            	}else{
            		day_count +=1;
            	};
            };
    	};
    };


    boost::gregorian::date scheduler::last_weekday(boost::date_time::weekdays day_of_week) const
    {
    	for (auto day=day_list.size(); day>0; day--){
            boost::gregorian::date given_date(year, month, day);
            if (given_date.day_of_week() == day_of_week) {
            	return given_date;
            };
    	};
    };
};
