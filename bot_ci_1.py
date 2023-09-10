import random
from i_player import IPlayer
from i_move import IMove
from i_chess_model_state import IChessModelState
from bot_utils import getRandomSpotToMoveFrom, getHighestCaptureMove, getMovesFromSpot

# An AI player where will choose a random piece to move, and that piece will try to capture 
# the maximum value piece
class BotCI1(IPlayer):
    def __init__(self, state : IChessModelState, show_debug : bool = True) -> None:
        self.state = state
        self.show_debug = show_debug

    def getNextMove(self) -> IMove:
        spot = getRandomSpotToMoveFrom(self.state)
        if (self.show_debug):
            print("Spot chosen by Bot 1: " + spot.getSpotAsString())
        maxCaptureMove = getHighestCaptureMove(self.state, spot)
        if maxCaptureMove is None:
            moves = getMovesFromSpot(self.state, spot)
            result = moves[random.randint(0, len(moves) - 1)]
            if (self.show_debug):
                print("Non capture move selected")
        else:
            result = maxCaptureMove
            if (self.show_debug):
                print("Max capture move selected")
        if (self.show_debug):
            print("Move chosen by Bot 1: " + result.getMoveAsString())
        return result