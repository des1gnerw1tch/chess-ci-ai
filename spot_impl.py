from i_spot import ISpot

# A spot on a chessboard. The column is a letter, a-h, and the row is a number, 
# 1-8 (inclusive).
class SpotImpl(ISpot):
    row = None
    col = None
    
    def __init__(self, col, row):
        if col not in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            raise ValueError("Column must be a string from a-h")
        if row < 1 or row > 8:
            raise ValueError("Row must be between 1-8, inclusive")
        self.row = str(row)
        self.col = col
        

    def getRow(self) -> str:
        return self.row

    def getCol(self) -> str:
        return self.col