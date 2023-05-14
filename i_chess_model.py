from abc import ABCMeta, abstractmethod

from i_chess_model_state import IChessModelState
from i_move import IMove

# A player in chess... Could be AI or Human.
class IChessModel(IChessModelState, metaclass = ABCMeta):
    
    # Moves a piece, accepts pseudo legal moves
    @abstractmethod
    def movePiece(self, move: IMove) -> None:
        pass