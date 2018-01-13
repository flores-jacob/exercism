def flatten(iterable):

    if type(iterable) is list:
        if len(iterable) > 0:
            return flatten(iterable[0]) + (flatten(iterable[1:]))
        else:
            return []
    else:
        if (iterable is not None) and (iterable != ()):
            return [iterable]
        else:
            return []

