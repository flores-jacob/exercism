def transpose(input_lines):

    output = []

    for input_row_index, input_row in enumerate(input_lines.split("\n")):
        for char_index, char in enumerate(input_row):
            try:
                output[char_index].append(char)
            except IndexError:
                output.append([char])

    return "\n".join(["".join(output_row) for output_row in output])