from i_ascii_chess_view import IAsciiChessView

from i_chess_model_state import IChessModelState
from i_move import IMove
from i_spot import ISpot

#Purpose: Display board, valid moves...
class IAsciiChessViewImpl(IAsciiChessView):
    validMoves = None
    boardAscii = None
    state = None
    hide_view = None

    # IChessViewImpl constructor
    # Returns: None
    def __init__(self, state:IChessModelState, hide_view : bool = False):
        self.state = state
        self.hide_view = hide_view

    # printBoard
    # Purpose: print ASCII view of board
    # Returns: None
    def printBoard(self):
        if (self.hide_view):
            return
        print(self.state.printAsciiViewIfAvailable())

    # printValidMoves
    # Purpose: print valid moves
    # Returns: None
    def printValidMoves(self):
        if (self.hide_view):
            return
        print(self.state.getValidMoves())