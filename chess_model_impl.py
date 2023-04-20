from i_chess_model import IChessModel
from i_spot import ISpot
from i_chess_model_state import Piece, GameOverStatus
from i_move import IMove
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
        pass

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
    