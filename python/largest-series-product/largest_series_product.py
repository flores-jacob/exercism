def largest_product(series, size):
    if size < 0:
        raise ValueError("size cannot be negative")
    elif size > len(series):
        raise ValueError("size should not exceed series length")

    product = 0
    for i in range(len(series) - (size - 1)):
        substring = series[i:i + size]
        current_product = 1
        for element in substring:
            current_product *= int(element)

        if current_product > product:
            product = current_product

    return product