from i_move import IMove
from i_spot import ISpot

# Current Spot (location) and target Spot (destination). 
class MoveImpl(IMove):
    location = None
    destination = None

    # MoveImpl constructor
    # Arguments: a Spot location, a Spot destination
    # Purpose: Initialize location and destination Spots
    def __init__(self, locationSpot, destinationSpot):
        self.location = locationSpot
        self.destination = destinationSpot
    
    # getDestination
    # Arguments: none
    # Purpose: Return target Spot destination of chess piece
    def getDestination(self):
        return self.destination
    
    # getLocation
    # Arguments: none
    # Purpose: Return current Spot location of chess piece
    def getLocation(self):
        return self.location
    
    def getMoveAsString(self) -> str:
        move = self.location.getSpotAsString() + self.destination.getSpotAsString()

        return move