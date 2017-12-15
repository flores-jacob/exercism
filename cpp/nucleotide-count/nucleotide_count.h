#include <iostream>
#include <string>
#include <map>
#include <stdexcept>

namespace dna {
    class counter
        {
            private:
                std::string dna_string;
                int A_counter;
                int T_counter;
                int C_counter;
                int G_counter;
            public:
                counter(std::string);
                std::map<char, int> nucleotide_counts() const;
                int count(char nucleotide) const;
        };

    // initialize and prep the input dna data as well as the initial counts
    counter::counter(std::string input_dna_string){
        dna_string = input_dna_string;

        A_counter = 0;
        T_counter = 0;
        C_counter = 0;
        G_counter = 0;

        for (int i=0; i<dna_string.length(); i++){
            if (dna_string.at(i) == 'A'){
                A_counter += 1;
            }else if (dna_string.at(i) == 'T'){
                T_counter += 1;
            }else if (dna_string.at(i) == 'C'){
                C_counter += 1;
            }else if (dna_string.at(i) == 'G'){
                G_counter += 1;
            }else {
                //throw an error if we encounter a non nucleotide
                std::string error_message;
                error_message = "A non nucleotide " + dna_string.at(i);
                error_message +=  " is found to be part of the dna string";
                throw std::invalid_argument(error_message);
            };
        };
    };

    // return the counts of all the nucleotides
    std::map<char, int> counter::nucleotide_counts() const
    {
        return { {'A', A_counter}, {'T', T_counter}, {'C', C_counter}, {'G', G_counter} }; 
    };

    // return the count of one specified nucleotide
    int counter::count(char nucleotide) const
    {
        int nucleotide_count;

        if (nucleotide == 'A'){
            nucleotide_count = A_counter;
        }else if (nucleotide == 'T'){
            nucleotide_count = T_counter;
        }else if (nucleotide == 'C'){
            nucleotide_count = C_counter;
        }else if (nucleotide == 'G'){
            nucleotide_count = G_counter;
        }else {
            throw std::invalid_argument("Please specify A, T, C, or G");
        };

        return nucleotide_count;
    };

};
