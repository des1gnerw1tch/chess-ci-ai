from i_player import IPlayer
from i_move import IMove
from i_spot import ISpot

# A spot on a chessboard. The column is a letter, a-h, and the row is a number, 
# 1-8 (inclusive).
class HumanCLIPlayer(IPlayer):

    #TODO: 
    def getNextMove() -> IMove:

        print("From spot? (i.e a6)")

        print("To spot? (i.e a7)")

        pass