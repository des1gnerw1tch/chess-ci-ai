from abc import ABCMeta, abstractmethod

from i_move import IMove

# A player in chess... Could be AI or Human.
class IPlayer(metaclass = ABCMeta):
    
    @abstractmethod
    def getNextMove() -> IMove:
        pass