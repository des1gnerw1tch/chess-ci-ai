import random
from i_player import IPlayer
from i_move import IMove
from i_chess_model_state import IChessModelState

# An AI player that just moves randomly.
class AIRandomMovesPlayer(IPlayer):
    state : IChessModelState

    def __init__(self, state : IChessModelState) -> None:
        self.state = state

    def getNextMove(self) -> IMove:
        listOfMoves = self.state.getValidMoves()
        move = listOfMoves[random.randint(0, len(listOfMoves) - 1)]
        #print(move.getMoveAsString())
        return move