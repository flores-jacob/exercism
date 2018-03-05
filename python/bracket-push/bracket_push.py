def brackets_match(opening_bracket, closing_bracket):
    bracket_dict = {"(": ")", "[": "]", "{": "}"}
    return bracket_dict[opening_bracket] == closing_bracket


def is_paired(input_string):
    bracket_stack = []
    # Add every "opening" bracket to the stack
    # if we encounter a "closing" bracket, it should match the current
    # bracket on top of the stack
    for char in input_string:
        # If we encounter an opening bracket, we add it on top of the stack
        if (char == "(") or (char == "[") or (char == "{"):
            bracket_stack.append(char)
        elif (char == ")") or (char == "]") or (char == "}"):
            # Get the bracket on top of the stack
            try:
                top_of_stack = bracket_stack.pop()
            # If the bracket_stack is empty, then we return false, since
            # the closing bracket has no opening bracket pair
            except IndexError:
                return False

            # Check and return if the opening and closing brackets match
            return brackets_match(top_of_stack, char)

    # Once done processing the string, bracket_stack should be empty
    # If empty, this means that all brackets have been matched
    # If not empty, this means that some brackets remain unmatched
    return bracket_stack == []
