#include <vector>
#include <set>
namespace sum_of_multiples
{
    int to(std::vector<int> vector_of_factors, int upto){

        std::set<int> factor_list;

        int multiple_sum = 0;

        for (int factor : vector_of_factors){
            for (int i=1; i<upto; i++){

                if (i % factor == 0){
                    factor_list.insert(i);
                };
            };
        };

        for (int multiple : factor_list){
            multiple_sum += multiple;
        };

        return multiple_sum;
    };


};
