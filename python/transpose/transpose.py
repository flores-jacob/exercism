

def transpose(input_lines):
    input_rows = input_lines.split("\n")

    # Get max number of columns from input_lines
    # This will serve as the number of rows
    max_row_len = max((len(row) for row in input_rows))

    # Prepare all candidate blank rows and blank elements
    output = []
    for output_row in range(max_row_len):
        output.append([' ' for _ in input_rows])

    # Loop through each row from the input
    # Assign each char into its transposed location
    for input_row_index, input_row in enumerate(input_rows):
        for char_index, char in enumerate(input_row):
            output[char_index][input_row_index] = char

    # Convert the list elements into strings in the output list
    concatenated_rows = ["".join(output_row) for output_row in output]

    # This will represent the max length of the strings we have encountered
    # so far while iterating backwards
    current_max_row_len = 0

    # Iterate backwards through the list
    for i in range(len(concatenated_rows) - 1, -1, -1):
        # Count what the length of the string is absent whitespace to the
        # right
        current_row_len = len(concatenated_rows[i].rstrip())

        # If the amount of non whitespace characters is greater than
        # the previous strings, then we assign it as the new
        # current_max_row_len
        if current_row_len > current_max_row_len:
            current_max_row_len = current_row_len

        # Remove all whitespace to the right of the string, then we
        # Add whitespace to the right of the string, depending on how
        # much shorter the string is to the current_max_row_len
        num_missing_spaces = current_max_row_len - current_row_len
        concatenated_rows[i] = concatenated_rows[i].rstrip() + (" " * num_missing_spaces)

    return "\n".join(concatenated_rows)
