from abc import ABCMeta, abstractmethod

# from i_spot import ISpot

# Current spot (location) and target spot (destination)
class IMove(metaclass = ABCMeta):
    @abstractmethod
    def getLocation():
        pass

    @abstractmethod
    def getDestination():
        pass
