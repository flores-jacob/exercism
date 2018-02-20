def saddle_points(matrix):
    saddle_point_list = []
    # Iterate through each row, noting the indices
    for row_index, row in enumerate(matrix):
        # iterate through each element, noting the indices
        for col_index, element in enumerate(row):

            # Attempt to get the column values for this particular element
            try:
                col_vals = [row2[col_index] for row2 in matrix]
            # If there's a mismatch in the row and column lengths, raise
            # a ValueError
            except IndexError:
                raise ValueError("Irregular matrix")

            # If the element has the highest value in its row, and the
            # lowest value in its column, then append it as a saddle
            # point onto the results
            if (element == max(row)) and (element == min(col_vals)):
                saddle_point_list.append((row_index, col_index))

    return set(saddle_point_list)
