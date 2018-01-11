def largest_product(series, size):
    product = 0
    for i in range(len(series) - (size - 1)):
        substring = series[i:i + size]
        current_product = 1
        for element in (list(map(int, substring))):
            current_product *= element

        if current_product > product:
            product = current_product

    return product