class Queen(object):
    def __init__(self, row, column):
        if (0 <= row <= 7) and (0 <= column <= 7):
            self.row = row
            self.column = column
        else:
            raise ValueError("Invalid row and column")

    def can_attack(self, another_queen):

        if (self.row == another_queen.row) and (self.column == another_queen.column):
            raise ValueError("Both queens occupy the same place")

        diff_row = abs(self.row - another_queen.row)
        diff_column = abs(self.column - another_queen.column)

        if (diff_column == 0) or (diff_row == 0) or (diff_row == diff_column):
            return True
        else:
            return False
