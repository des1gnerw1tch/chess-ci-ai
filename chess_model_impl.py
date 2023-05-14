from i_chess_model import IChessModel
from i_spot import ISpot
from i_chess_model_state import Piece, GameOverStatus
from i_move import IMove
from move_impl import MoveImpl
from spot_impl import SpotImpl
from typing import List
from chess import Board, Move, WHITE, BLACK

# This model implements chess with the "chess" python module. A great descriptive name
# for a chess module!
class ChessModelImpl(IChessModel):
    chess_board = None
    
    def __init__(self) -> None:
        self.chess_board = Board()

    def getPieceAtSpot(self, spot: ISpot) -> Piece:
        pass

    def getValidMoves(self) -> List[IMove]:
        legalMoves = list(self.chess_board.legal_moves)

        myLegalMoves = list()

        for move in legalMoves:
            fromSpot = SpotImpl((move.uci())[0], int((move.uci())[1]))
            toSpot = SpotImpl((move.uci())[2], int((move.uci())[3]))

            myMove = MoveImpl(fromSpot, toSpot)

            myLegalMoves.append(myMove.getMoveAsString())

        return myLegalMoves

    def getGameOverStatus(self) -> GameOverStatus:
        outcome = self.chess_board.outcome()
        if outcome is None:
            return GameOverStatus.IN_PROGRESS

        color = outcome.winner
        if color == WHITE:
            return GameOverStatus.WHITE_WIN
        elif color == BLACK:
            return GameOverStatus.BLACK_WIN
        elif color is None:
            return GameOverStatus.DRAW

    def isInCheck(self) -> bool:
        return self.chess_board.is_check()

    def movePiece(self, move: IMove) -> None:
        pass

    def printAsciiViewIfAvailable() -> str:
        pass
    