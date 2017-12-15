#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
namespace grade_school
{
    class school{
        private:
            std::map<int, std::vector<std::string>> roster_;
        public:
            school();
            std::map<int, std::vector<std::string>> roster();
            void add(std::string name, int grade);
            std::vector<std::string> grade(int grade_input);

    };
    // std::map<int, std::vector<std::string>> school

    school::school()
    {
        roster_ = {};
    };

    std::map<int, std::vector<std::string>> school::roster()
    {
        return roster_;
    };

    void school::add(std::string name, int grade)
    {
        // add the name to the grade
        roster_[grade].push_back(name);
        // resort the names for the grade
        std::sort(roster_[grade].begin(), roster_[grade].end());
    };

    std::vector<std::string> school::grade(int grade_input)
    {
        if (roster_.count(grade_input))
        {
            return roster_[grade_input];
        }else{
            return {};
        };
    };    

};


