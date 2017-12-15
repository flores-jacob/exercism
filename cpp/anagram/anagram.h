#include <string>
#include <vector>


namespace anagram{
    class anagram
    {
        private:
            std::string string_input;

        public:
            anagram(std::string string_input);
            auto matches(std::vector<std::string> string_list) -> std::vector<std::string>;
    };
};
