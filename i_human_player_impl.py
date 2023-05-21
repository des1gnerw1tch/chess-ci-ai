from i_player import IPlayer

from i_move import IMove
from move_impl import MoveImpl
from spot_impl import SpotImpl
from i_chess_model_state import IChessModelState

class HumanPlayerImpl(IPlayer):

    def getNextMove(self) -> IMove:
        fromSpot = input("From (e.g. \"e4\"): ")
        toSpot = input ("To (e.g. \"e5\"): ")

        move = MoveImpl(SpotImpl(fromSpot[0], int(fromSpot[1])), 
                        SpotImpl(toSpot[0], int(toSpot[1])))

        return move