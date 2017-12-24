#include <string>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
namespace allergies
{
    class allergy_test
    {
        private:
            std::vector<std::string> allergen_masterlist = {"eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"};
            std::vector<std::string> allergen_patientlist;

        public:
            allergy_test(float allergy_score);
            bool is_allergic_to(std::string allergen);
    };

    allergy_test::allergy_test(float allergy_score)
    {
        // discontinue if allergy score is zero
        if (allergy_score == 0){
            return;
        };

        while (allergy_score > 0){
            // get the log2 of the score
            float exponent = log2 (allergy_score);
            // check if this log2 is a whole number.
            if (floor(exponent) == exponent){
            // If it is, then the exponent represents the index of the allergy in the masterlist
                allergen_patientlist.push_back(allergen_masterlist.at(exponent));
            }else if (floor(exponent) != exponent){
            // If it is not, then round it down, and check what allergy the rounded down index represents
            // if it represents an allergy, add it to a list of allergens
                // check first if the index is less than the vector size
                if (floor(exponent) < allergen_masterlist.size()){
                    // if it is, then add the identified allergen to the list
                    allergen_patientlist.push_back(allergen_masterlist.at(floor(exponent)));
                };

//                allergy_score -= allergy_score - pow(2, floor(exponent));
            };
            // subtract this value from the total score, regardless of whether or not the allergen is in the masterlist
            allergy_score = allergy_score - pow(2, floor(exponent));
            std::cout << allergy_score << std::endl;
        };
    };

    bool allergy_test::is_allergic_to(std::string allergen)
    {
        if (std::find(allergen_patientlist.begin(), allergen_patientlist.end(), allergen) != allergen_patientlist.end()){
            return true;
        }

        return false;
    };

};