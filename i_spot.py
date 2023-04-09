from abc import ABCMeta, abstractmethod

class iSpot(metaclass = ABCMeta):
    @abstractmethod
    def getRow() -> str:
        pass

    @abstractmethod
    def getCol() -> str:
        return "yee"