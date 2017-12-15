#include <string>
#include <map>
#include <locale>
namespace scrabble_score
{
    std::map<char, int> scores{
        {'a', 1}, {'b', 3},  {'c', 3}, {'d', 2}, {'e', 1},
        {'f', 4}, {'g', 2},  {'h', 4}, {'i', 1}, {'j', 8},
        {'k', 5}, {'l', 1},  {'m', 3}, {'n', 1}, {'o', 1},
        {'p', 3}, {'q', 10}, {'r', 1}, {'s', 1}, {'t', 1},
        {'u', 1}, {'v', 4},  {'w', 4}, {'x', 8}, {'y', 4},
        {'z', 10}
    };

    int score(std::string word)
    {

        std::string lower_case_word;
        // convert the input string to lower case
        for (char elem: word){
            lower_case_word += std::tolower(elem);
        };

        char letter;
        int total_score = 0;
        for (int i=0; i < lower_case_word.length(); i++){
            letter = lower_case_word[i];
            total_score += scores[letter];
        };
        return total_score;
    };

};
