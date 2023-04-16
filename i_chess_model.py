from abc import ABCMeta, abstractmethod

from i_chess_model_state import IChessModelState
from i_move import IMove

# A player in chess... Could be AI or Human.
class IChessModel(IChessModelState, metaclass = ABCMeta):
    
    @abstractmethod
    def movePiece(self, move: IMove) -> None:
        pass