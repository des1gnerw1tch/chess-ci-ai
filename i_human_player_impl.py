from i_player import IPlayer

from i_move import IMove
from move_impl import MoveImpl
from spot_impl import SpotImpl
from i_chess_model_state import IChessModelState
from i_chess_model_state import Piece

class HumanPlayerImpl(IPlayer):
    promotionType = None
    promotionPiece = None

    # Name:    getNextMove
    # Purpose: Prompt user for location and destination spots and promotion
    #          if applicable.
    # Return:  a player IMove
    def getNextMove(self, boardState : IChessModelState) -> IMove:
        fromSpot = input("From (e.g. \"e4\"): ")
        toSpot = input ("To (e.g. \"e5\"): ")

        # check if piece needs to be promoted
        if (int(toSpot[1]) == 8 or int(toSpot[1]) == 1):
            if (boardState.getPieceAtSpot(SpotImpl(fromSpot[0], int(fromSpot[1]))) == Piece.PAWN):
                self.promotionType = input("Promote pawn to: ")
            
            if (self.promotionType[1].lower() == 'n'):
                self.promotionPiece = Piece.KNIGHT
            elif (self.promotionType[0].lower() == 'q'):
                self.promotionPiece = Piece.QUEEN
            elif (self.promotionType[0].lower() == 'b'):
                self.promotionPiece = Piece.BISHOP
            elif (self.promotionType[0].lower() == 'k'):
                self.promotionPiece = Piece.KING
            elif (self.promotionType[0].lower() == 'p'):
                self.promotionPiece = Piece.PAWN
            elif (self.promotionType[0].lower() == 'r'):
                self.promotionPiece = Piece.ROOK

        # store move with or without promotion type
        move = MoveImpl(SpotImpl(fromSpot[0], int(fromSpot[1])), 
                SpotImpl(toSpot[0], int(toSpot[1])), self.promotionPiece)

        return move