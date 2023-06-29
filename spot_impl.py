from i_spot import ISpot
import math

# A spot on a chessboard. The column is a letter, a-h, and the row is a number, 
# 1-8 (inclusive).
class SpotImpl(ISpot):
    row = None
    col = None
    
    def __init__(self, col : str, row : int):
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
    
    def getSpotAsString(self) -> str:
        self.spot = self.col + self.row

        return self.spot
    
    def equals(self, spot : ISpot) -> bool:
        return self.getRow() == spot.getRow() and self.getCol() == spot.getCol()

    # Name:    distanceTo
    # Purpose: find distance, in squares, from location to destination 
    # Returns: return distance as float
    def distanceTo(self, spot : 'ISpot') -> float: 
        rowTo = float(int(spot.getRow()))
        columnToAsInt = float(ord(spot.getCol()) - 96.0)

        rowDifference = rowTo - float(self.row)
        columnDifference = columnToAsInt - float((ord(self.col) - 96.0))

        distance = math.sqrt(columnDifference**2.0 + rowDifference**2.0)

        return distance

    # Name:    distanceToNorm
    # Purpose: normalize distance to 0-1 scale. 0 represents maximum 
    #          possible distance (e.g. a1 to h8). 1 represents minimum possible 
    #          distance (e.g. a1 to a2).
    # Returns: distance normalized on a 0-1 scale
    def distanceToNorm(self, spot : 'ISpot') -> float:
        # max distance is from one corner-to-corner length of board
        max = math.sqrt((49) + (49))
        # min distance is 1 square (NOTE: not 0 squares)
        min = 1

        # Get distance
        distance = self.distanceTo(spot)

        # Get normalized distance
        normalized = (max - distance)/(max - min)

        return normalized