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