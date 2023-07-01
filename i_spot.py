from abc import ABCMeta, abstractmethod

# A spot on the chess board. 
class ISpot(metaclass = ABCMeta):
    @abstractmethod
    def getRow() -> str:
        pass

    @abstractmethod
    def getCol() -> str:
        pass
    
    @abstractmethod
    def getSpotAsString() -> str:
        pass

    @abstractmethod
    def equals(spot : 'ISpot') -> bool:
        pass

    @abstractmethod
    def distanceTo(spot: 'ISpot') -> float:
        """
        Gets the distance in squares from this spot to another spot, using
        the distance formula
        """
        pass

    @abstractmethod
    def distanceToNorm(spot: 'ISpot') -> float:
        """
        Returns a normalized value between 0-1, 0 representing the max 
        distance away on chess board, and 1 representing closest distance 
        two spots can be away from each other on chess board
        """
        pass