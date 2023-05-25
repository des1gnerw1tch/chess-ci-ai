from i_player import IPlayer

from i_move import IMove
from move_impl import MoveImpl
from spot_impl import SpotImpl
from i_chess_model_state import IChessModelState
from i_chess_model_state import Piece

class HumanPlayerImpl(IPlayer):
    promotionType = None

    def getNextMove(self, boardState: IChessModelState) -> IMove:
        fromSpot = input("From (e.g. \"e4\"): ")
        toSpot = input ("To (e.g. \"e5\"): ")

        if (toSpot[1] == 8 or toSpot[1] == 1):
            if (boardState.getPieceAtSpot(SpotImpl(fromSpot[0], fromSpot[1])) == Piece.PAWN):
                promotionType = input("Promote pawn to: ")

        move = MoveImpl(SpotImpl(fromSpot[0], int(fromSpot[1])), 
                        SpotImpl(toSpot[0], int(toSpot[1])))

        return move