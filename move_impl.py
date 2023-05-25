from i_move import IMove
from i_spot import ISpot
from piece import Piece

# Current Spot (location) and target Spot (destination). 
class MoveImpl(IMove):
    location = None
    destination = None
    promotion = None

    # MoveImpl constructor
    # Arguments: a Spot location, a Spot destination
    # Purpose: Initialize location and destination Spots
    def __init__(self, locationSpot, destinationSpot, promotion : Piece = None):
        self.location = locationSpot
        self.destination = destinationSpot
        self.promotion = promotion

    def getDestination(self):
        return self.destination
    
    def getLocation(self):
        return self.location

    def getPromotionTypeIfAvailable(self) -> Piece:
        return self.promotion
    
    def getMoveAsString(self) -> str:
        move = self.location.getSpotAsString() + self.destination.getSpotAsString()

        return move