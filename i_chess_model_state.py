from abc import ABCMeta, abstractmethod
from i_move import IMove
from typing import List
from spot_impl import ISpot
from game_over_status import GameOverStatus
from piece import Piece
from player_color import PlayerColor

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

    # Get the ID of a piece depending on the spot. If spot does not have
    # piece, will return -1
    @abstractmethod
    def getPieceIDFromSpot(self, spot : ISpot) -> int:
        pass

    # Gets the spot of a piece ID. If piece does not exist (has been captured),
    # will return None
    @abstractmethod
    def getSpotByPieceID(self, id : int) -> ISpot:
        pass
