from abc import ABCMeta, abstractmethod

# A spot on the chess board. 
class ISpot(metaclass = ABCMeta):
    @abstractmethod
    def getRow() -> str:
        pass

    @abstractmethod
    def getCol() -> str:
        pass