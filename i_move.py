from abc import ABCMeta, abstractmethod
from i_spot import ISpot

# from i_spot import ISpot

# Current spot (location) and target spot (destination)
class IMove(metaclass = ABCMeta):
    @abstractmethod
    def getLocation() -> ISpot:
        pass

    @abstractmethod
    def getDestination() -> ISpot:
        pass
