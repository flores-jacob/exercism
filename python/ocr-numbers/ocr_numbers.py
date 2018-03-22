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

    num_chunks = int(len(input_grid[0]) / 3)

    chunk_list = []

    for num_chunk in range(num_chunks):

        beginning_index = 3 * num_chunk
        end_index = beginning_index + 3

        chunk = [
            "".join([char for char in input_grid[0][beginning_index:end_index]]),
            "".join([char for char in input_grid[1][beginning_index:end_index]]),
            "".join([char for char in input_grid[2][beginning_index:end_index]]),
            "".join([char for char in input_grid[3][beginning_index:end_index]])
        ]

        chunk_val = "?"

        for index, chunk_candidate in enumerate(chunk_reference):
            if chunk_candidate == chunk:
                chunk_val = str(index)
                break

        chunk_list.append(chunk_val)

    return "".join(chunk_list)
