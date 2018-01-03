def slices(series, length):
    series_list = []

    if length == 0:
        raise ValueError("Cannot have a length of 0")
    elif len(series) < length:
        raise ValueError("Desired length exceeds series length")

    for index in range(len(series)):
        appendable_list = [int(x) for x in series[index:index + length]]
        if len(appendable_list) == length:
            series_list.append(appendable_list)
    return series_list