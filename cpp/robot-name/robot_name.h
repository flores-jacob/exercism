#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

namespace robot_name
{
    class robot
    {
        private:
            std::vector<std::string> letters_ = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
            std::vector<std::string> numbers_ = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"};
            std::string name_;
            std::vector<std::string> taken_names_ = {};
        public:
            robot();
            std::string name() const;
            std::string generate_name();
            void reset();
    };


    std::string robot::generate_name()
    {
        std::random_shuffle(letters_.begin(), letters_.end());
        std::random_shuffle(numbers_.begin(), numbers_.end());
        return letters_[0] + letters_[1] + numbers_[0] + numbers_[1] + numbers_[2];
    };


    void robot::reset()
    {
        // generate a random name
        name_ = generate_name();
        // while the name can be found in the list of taken names, continue generating new names
        while (std::find(taken_names_.begin(), taken_names_.end(), name_) != taken_names_.end()){
            name_ = generate_name();
        };
        // once we have a new name, add the name on to the taken list
        taken_names_.push_back(name_);
    };

    robot::robot()
    {
        reset();
    };

    std::string robot::name() const
    {
        return name_;
    };


};
