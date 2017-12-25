#include <string>
#include <vector>

namespace bracket_push
{
    bool bracket_match(char opening_bracket, char closing_bracket){
        if (opening_bracket == '(' && closing_bracket != ')'){
            return false;
        }else if (opening_bracket == '{' && closing_bracket != '}'){
            return false;
        } else if (opening_bracket == '[' && closing_bracket != ']'){
            return false;
        } else {
            return true;
        };
    };
    bool check(std::string input_brackets)
    {
        std::vector<char> bracket_stack;
        // for every "opening" bracket, add it to the stack
        // if we encounter a "closing" bracket, it should match the current
        // bracket on top of the stack
        for (int i=0; i<input_brackets.length(); i++){
            char current_char = input_brackets.at(i);
            // if we encounter an opening bracket, we add it on top of the stack
            if (current_char == '(' || current_char == '{' || current_char == '['){
                bracket_stack.push_back(current_char);
            } else if (current_char == ')' || current_char == '}' || current_char == ']'){
                // if the bracket_stack is empty, and we start with a closing bracket, then
                // we return false, as the first bracket has no pair
                if (bracket_stack.size() == 0){
                    return false;
                };

                // get the bracket on top of the stack
                char top_of_stack = bracket_stack.back();
                // check if the opening bracket is the same as the closing bracket
                // if they are not the same, then return false
                // if they are the same, continue
                if (!bracket_match(top_of_stack, current_char)){
                    return false;
                };
                // delete the topmost bracket item, since it has already been matched
                bracket_stack.pop_back();
            };
        };

        // once the for loop has finished, the bracket stack should be empty,
        // since all brackets have been matched. If it is not empty, then the brackets
        // are assymetrical, so we retrun false
        if (bracket_stack.size() > 0){
            return false;
        };

        // if the checks above did not detect any irregularities, we assert that the brackets
        // are symmetrical and match
        return true;
    };
};