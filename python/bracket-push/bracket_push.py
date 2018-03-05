def brackets_match(opening_bracket, closing_bracket):
    bracket_dict = {"(": ")", "[": "]", "{": "}"}
    return bracket_dict[opening_bracket] == closing_bracket


def is_paired(input_string):
    bracket_stack = []

    for char in input_string:
        if (char == "(") or (char == "[") or (char == "{"):
            bracket_stack.append(char)
        elif (char == ")") or (char == "]") or (char == "}"):
            if len(bracket_stack) == 0:
                return False

            top_of_stack = bracket_stack.pop()

            return brackets_match(top_of_stack, char)

    if len(bracket_stack) > 0:
        return False

    return True
