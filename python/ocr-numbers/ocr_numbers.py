def convert(input_grid):

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

