def board(input_board_array):
    output_board = []
    prev_row_len = None
    # Loop through each row, noting the index
    for row_index, row in enumerate(input_board_array):
        output_row = []
        row_len = len(row)

        # Check if the current row has the same length as the previous row
        if prev_row_len:
            if prev_row_len != row_len:
                raise ValueError("unequal row lengths")

        # Loop through each element, noting the index
        for elem_index, elem in enumerate(row):
            # If the current element is a blank space, we compute the number
            # of asterisks around it
            if elem == " ":
                # We get the row on top of the current row
                if row_index > 0:
                    top_row = input_board_array[row_index - 1]
                # If the current row is the first row, then there is
                # no top row
                else:
                    top_row = []

                # We get the row beneath the current row
                if row_index < len(input_board_array) - 1:
                    bottom_row = input_board_array[row_index + 1]
                # If the current row is the bottom row, then there is no
                # row beneath it
                else:
                    bottom_row = []

                # Sum number of asterisks on top of element
                top_row_sum = sum([1 for element in top_row[max(0, elem_index - 1): elem_index + 2] if element == "*"])
                # Sum number of asterisks beside element
                mid_row_sum = sum([1 for element in row[max(0, elem_index - 1): elem_index + 2] if element == "*"])
                # Sum number of asterisks beneath element
                bottom_row_sum = sum([1 for element in bottom_row[max(0, elem_index - 1): elem_index + 2] if element == "*"])

                # Sum all asterisks
                surrounding_mine_count = top_row_sum + mid_row_sum + bottom_row_sum

                # If there are asterisks, append the number into the output_row
                if surrounding_mine_count > 0:
                    output_row.append(str(surrounding_mine_count))
                # If no asterisks, append " " instead
                else:
                    output_row.append(" ")
            # If the current element is an asterisk, simply append it to
            # the output row
            elif elem == "*":
                output_row.append("*")
            # If the current element is niether an asterisk or a space,
            # then it is an invalid character
            else:
                raise ValueError("Invalid character")
        # Once the output row has been fully formed, convert it into a string
        # and append it onto the output board
        output_board.append("".join(output_row))
        # Assign the row_len as the previous row len for error checking
        prev_row_len = row_len
    return output_board
