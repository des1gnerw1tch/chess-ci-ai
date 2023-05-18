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
    BLANK = 0
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6

class PlayerColor(Enum):
    WHITE = 0
    BLACK = 1

# The state of the chess game
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
    
    # Returns if either team is in check
    @abstractmethod
    def isInCheck(self) -> bool:
        pass

    @abstractmethod
    def printAsciiViewIfAvailable(self) -> str:
        pass
    
    # If move is legal, not including pseudo legal moves. Takes into account whose 
    # turn it is.
    @abstractmethod
    def isMoveLegal(self, move: IMove) -> bool:
        pass

    # Return whose turn it is in the game
    @abstractmethod
    def getWhoseTurn(self) -> PlayerColor:
        pass
