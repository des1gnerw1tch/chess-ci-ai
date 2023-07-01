import random
from i_player import IPlayer
from i_move import IMove
from i_chess_model_state import IChessModelState
from bot_utils import getRandomSpotToMoveFrom, getHighestCaptureMove, getMovesFromSpot

# An AI player where will choose a random piece to move, and that piece will try to capture 
# the maximum value piece
class BotCI1(IPlayer):
    def __init__(self, state : IChessModelState) -> None:
        self.state = state

    def getNextMove(self) -> IMove:
        spot = getRandomSpotToMoveFrom(self.state)
        print("Spot chosen by Bot 1: " + spot.getSpotAsString())
        maxCaptureMove = getHighestCaptureMove(self.state, spot)
        if maxCaptureMove is None:
            moves = getMovesFromSpot(self.state, spot)
            result = moves[random.randint(0, len(moves) - 1)]
            print("Non capture move selected")
        else:
            result = maxCaptureMove
            print("Max capture move selected")
        print("Move chosen by Bot 1: " + result.getMoveAsString())
        return result