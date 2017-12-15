#include "hamming.h"
#include <stdexcept>


namespace hamming{
    int compute(std::string string_a, std::string string_b){

        if (string_a.length() != string_b.length()){

            throw std::domain_error("input dna strand lengths do not match");
        };

        int hamming_distance = 0;
    
        for(int i=0; i < string_a.length() ; i++){

            // option1 in accessing string elements
            // if (string_a[i] != string_b[i]){
            // option2 in accessing string elements
            if (string_a.at(i) != string_b.at(i)){
                hamming_distance = hamming_distance + 1;
            };
        };

        return hamming_distance;

    };
};

