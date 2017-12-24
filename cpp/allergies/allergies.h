#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <unordered_set>

namespace allergies
{
    class allergy_test
    {
        private:
            std::vector<std::string> allergen_masterlist = {"eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"};
            std::unordered_set<std::string> allergen_patientlist;

        public:
            allergy_test(float allergy_score);
            bool is_allergic_to(std::string allergen);
            std::unordered_set<std::string> get_allergies();
    };

    allergy_test::allergy_test(float allergy_score)
    {
        // while total allergy score has not been reduced to zero, continue to reduce it
        while (allergy_score > 0){
            // get the log2 of the score
            float exponent = log2 (allergy_score);

            // if it represents an allergy, add it to a list of allergens
            // check first if the index is less than the vector size
            if (floor(exponent) < allergen_masterlist.size()){
                // if it is, then add the identified allergen to the list
                allergen_patientlist.insert(allergen_masterlist.at(floor(exponent)));
            };
            // subtract the round score from the total allergy score, then loop again
            allergy_score = allergy_score - pow(2, floor(exponent));
        };
    };

    bool allergy_test::is_allergic_to(std::string allergen)
    {
        if (std::find(allergen_patientlist.begin(), allergen_patientlist.end(), allergen) != allergen_patientlist.end()){
            return true;
        }

        return false;
    };

    std::unordered_set<std::string> allergy_test::get_allergies(){
        return allergen_patientlist;
    };

};