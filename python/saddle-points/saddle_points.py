def saddle_points(matrix):
    saddle_point_list = []
    for row_index, row in enumerate(matrix):
        for col_index, element in enumerate(row):

            try:
                col_vals = [row2[col_index] for row2 in matrix]
            except IndexError:
                raise ValueError("Irregular matrix")

            if (element == max(row)) and (element == min(col_vals)):
                saddle_point_list.append((row_index, col_index))

    return set(saddle_point_list)
