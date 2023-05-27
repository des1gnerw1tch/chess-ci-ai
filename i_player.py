from abc import ABCMeta, abstractmethod

from i_move import IMove
from i_chess_model_state import IChessModelState

# A player in chess... Could be AI or Human.
class IPlayer(metaclass = ABCMeta):
    
    @abstractmethod
    def getNextMove(self) -> IMove:
        pass