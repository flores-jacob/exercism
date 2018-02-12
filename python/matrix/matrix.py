class Matrix(object):
    def __init__(self, matrix_string):
        # Use splitlines() instead of split('\n')
        self.rows = [list(map(int, row.split())) for row in matrix_string.splitlines()]
        # Use list comprehension instead of map() for greater readability
        self.columns = [list(column) for column in zip(*self.rows)]
