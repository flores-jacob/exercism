

def transpose(input_lines):
    input_rows = input_lines.split("\n")

    max_row_len = max((len(row) for row in input_rows))

    output = []

    for input_row in input_rows:
        for index in range(max_row_len):
            try:
                char = input_row[index]
            except IndexError:
                char = " "

            try:
                output[index].append(char)
            except IndexError:
                output.append([char])

    concatenated_rows = ["".join(output_row) for output_row in output]

    current_max_row_len = 0

    for i in range(len(concatenated_rows) - 1, -1, -1):
        current_row_len = len(concatenated_rows[i].rstrip())

        if current_row_len > current_max_row_len:
            current_max_row_len = current_row_len

        concatenated_rows[i] = concatenated_rows[i].rstrip() + (" " * (current_max_row_len - current_row_len))

    return "\n".join(concatenated_rows)
