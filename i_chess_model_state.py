from abc import ABCMeta, abstractmethod
from i_move import IMove
from typing import List
from spot_impl import ISpot

# TODO: Move these enums into their own modules/packages? Doesn't make sense
# to have them in the chess model state module. 
from enum import Enum

class GameOverStatus(Enum):
    IN_PROGRESS = 0
    WHITE_WIN = 1
    BLACK_WIN = 2
    DRAW = 3

class Piece(Enum):
    PAWN = 0
    ROOK = 1
    KNIGHT = 2
    BISHOP = 3
    QUEEN = 4
    KING = 5

# A spot on the chess board. 
class IChessModelState(metaclass = ABCMeta):
    @abstractmethod
    def getPieceAtSpot(self, spot: ISpot) -> Piece:
        pass

    @abstractmethod
    def getValidMoves(self) -> List[IMove]:
        pass

    @abstractmethod
    def getGameOverStatus(self) -> GameOverStatus:
        pass

    @abstractmethod
    def isInCheck(self) -> bool:
        pass

    @abstractmethod
    def printAsciiViewIfAvailable() -> str:
        pass
