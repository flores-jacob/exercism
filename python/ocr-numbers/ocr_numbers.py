def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines not multiple of 4")

    for row in input_grid:
        if len(row) % 3 != 0:
            raise ValueError("Row numbers not multiple of 3")

    chunk_reference = [
        [" _ ",
         "| |",
         "|_|",
         "   "],
        ["   ",
         "  |",
         "  |",
         "   "],
        [" _ ",
         " _|",
         "|_ ",
         "   "],
        [" _ ",
         " _|",
         " _|",
         "   "],
        ["   ",
         "|_|",
         "  |",
         "   "],
        [" _ ",
         "|_ ",
         " _|",
         "   "],
        [" _ ",
         "|_ ",
         "|_|",
         "   "],
        [" _ ",
         "  |",
         "  |",
         "   "],
        [" _ ",
         "|_|",
         "|_|",
         "   "],
        [" _ ",
         "|_|",
         " _|",
         "   "]
    ]

    num_horizontal_sets = int(len(input_grid)/4)

    num_chunks = int(len(input_grid[0]) / 3)

    horizontal_set_list = []

    for num_horizontal_set in range(num_horizontal_sets):
        horizontal_set = input_grid[4 * num_horizontal_set: (4 * num_horizontal_set) + 4]

        chunk_list = []

        for num_chunk in range(num_chunks):

            beginning_index = 3 * num_chunk
            end_index = beginning_index + 3

            chunk = [
                "".join([char for char in horizontal_set[0][beginning_index:end_index]]),
                "".join([char for char in horizontal_set[1][beginning_index:end_index]]),
                "".join([char for char in horizontal_set[2][beginning_index:end_index]]),
                "".join([char for char in horizontal_set[3][beginning_index:end_index]])
            ]

            chunk_val = "?"

            for index, chunk_candidate in enumerate(chunk_reference):
                if chunk_candidate == chunk:
                    chunk_val = str(index)
                    break

            chunk_list.append(chunk_val)

        horizontal_set_list.append("".join(chunk_list))

    return ",".join(horizontal_set_list)
