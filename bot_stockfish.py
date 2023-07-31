from stockfish import Stockfish
from i_move import IMove

from i_player import IPlayer
from i_chess_model_state import IChessModelState

class BotStockfish(IPlayer):
    """
    Bot that uses the Stockfish engine. 
    """

    def __init__(self, state : IChessModelState, elo : int, time_constraint : int = None) -> None:
        """
        time_constraint: maximum time of thinking in milliseconds
        """
        self.state = state
        self.elo = elo
        self.stockfish = Stockfish()
        self.stockfish.set_elo_rating(elo)
        #self.stockfish.set_skill_level(elo)
        self.time_constraint = time_constraint
        

    
    def getNextMove(self) -> IMove:
        # Set fen based on model state fen
        self.stockfish.set_fen_position(self.state.getFen())
        
        move = None
        if (self.time_constraint is not None):
            move = str(self.stockfish.get_best_move_time(self.time_constraint))
        else:
            move = str(self.stockfish.get_best_move())
        
        best_move = self.state.stockfishMoveToOurMove(move)
        print(best_move.getMoveAsString())
        return best_move
    
