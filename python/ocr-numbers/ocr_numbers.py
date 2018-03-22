def convert(input_grid):

    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines not multiple of 4")

    for row in input_grid:
        if len(row) % 3 != 0:
            raise ValueError("Row numbers not multiple of 3")

    chunk = input_grid

    chunk_list = [
        [" _ ",
         "| |",
         "|_|",
         "   "],
        ["   ",
         "  |",
         "  |",
         "   "]
    ]

    output = "?"

    for index, chunk_candidate in enumerate(chunk_list):
        if chunk_candidate == chunk:
            output = str(index)

    return output

