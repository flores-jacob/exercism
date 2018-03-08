def board(input_board_array):
    output_board = []
    prev_row_len = None
    for row_index, row in enumerate(input_board_array):
        output_row = []
        row_len = len(row)

        if prev_row_len:
            if prev_row_len != row_len:
                raise ValueError("unequal row lengths")

        for elem_index, elem in enumerate(row):
            if elem == " ":

                if row_index > 0:
                    top_row = input_board_array[row_index - 1]
                else:
                    top_row = []

                if row_index < len(input_board_array) - 1:
                    bottom_row = input_board_array[row_index + 1]
                else:
                    bottom_row = []

                top_row_sum = sum([1 for element in top_row[max(0, elem_index - 1): elem_index + 2] if element == "*"])
                mid_row_sum = sum([1 for element in row[max(0, elem_index - 1): elem_index + 2] if element == "*"])
                bottom_row_sum = sum([1 for element in bottom_row[max(0, elem_index - 1): elem_index + 2] if element == "*"])

                surrounding_mine_count = top_row_sum + mid_row_sum + bottom_row_sum

                if surrounding_mine_count > 0:
                    output_row.append(str(surrounding_mine_count))
                else:
                    output_row.append(" ")
            elif elem == "*":
                output_row.append("*")
            else:
                raise ValueError("Invalid character")
        output_board.append("".join(output_row))
        prev_row_len = row_len
    return output_board
