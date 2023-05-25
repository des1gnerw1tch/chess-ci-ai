from abc import ABCMeta, abstractmethod
from i_spot import ISpot
from piece import Piece

# Current spot (location) and target spot (destination)
class IMove(metaclass = ABCMeta):

    # getLocation
    # Arguments: none
    # Purpose: Return current Spot location of chess piece
    @abstractmethod
    def getLocation() -> ISpot:
        pass

    # getDestination
    # Arguments: none
    # Purpose: Return target Spot destination of chess piece
    @abstractmethod
    def getDestination() -> ISpot:
        pass

    @abstractmethod
    def getPromotionTypeIfAvailable() -> Piece:
        pass

    @abstractmethod
    def getMoveAsString() -> str:
        pass