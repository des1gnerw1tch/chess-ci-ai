from i_player import IPlayer

from i_move import IMove
from move_impl import MoveImpl
from spot_impl import SpotImpl
from i_chess_model_state import IChessModelState
from i_chess_model_state import Piece

class HumanPlayerImpl(IPlayer):
    boardState = None

    def __init__(self, boardState : IChessModelState):
        self.boardState = boardState

    # Name:    getNextMove
    # Purpose: Prompt user for location and destination spots and promotion
    #          if applicable.
    # Return:  a player IMove
    def getNextMove(self) -> IMove:
        promotionType = None
        promotionPiece = None
        fromSpot = input("From (e.g. \"e4\"): ")
        toSpot = input ("To (e.g. \"e5\"): ")

        # check if piece needs to be promoted
        if (int(toSpot[1]) == 8 or int(toSpot[1]) == 1):
            if (self.boardState.getPieceAtSpot(SpotImpl(fromSpot[0], int(fromSpot[1]))) == Piece.PAWN):
                promotionType = input("Promote pawn to: ")
            
                if (promotionType[1].lower() == 'n'):
                    promotionPiece = Piece.KNIGHT
                elif (promotionType[0].lower() == 'q'):
                    promotionPiece = Piece.QUEEN
                elif (promotionType[0].lower() == 'b'):
                    promotionPiece = Piece.BISHOP
                elif (promotionType[0].lower() == 'k'):
                    promotionPiece = Piece.KING
                elif (promotionType[0].lower() == 'p'):
                    promotionPiece = Piece.PAWN
                elif (promotionType[0].lower() == 'r'):
                    promotionPiece = Piece.ROOK

        # store move with or without promotion type
        move = MoveImpl(SpotImpl(fromSpot[0], int(fromSpot[1])), 
                SpotImpl(toSpot[0], int(toSpot[1])), promotionPiece)

        return move