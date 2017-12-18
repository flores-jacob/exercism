#include <string>

namespace transcription {

    char to_rna(char dna_input)
    {
        switch(dna_input)
            {
            case 'G': return 'C';
            case 'C': return 'G';
            case 'A': return 'U';
            case 'T': return 'A';
            }

        // raise an error if input is malformed
        return 1;
    };

    std::string to_rna(std::string dna_input)
    {
        std::string rna_output;
        for (char elem: dna_input)
        {
            rna_output += to_rna(elem);
        };

        return rna_output;
    };


};