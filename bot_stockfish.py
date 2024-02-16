from stockfish import Stockfish
from i_move import IMove
from argparse import ArgumentError
from random import randint, uniform

from i_player import IPlayer
from i_chess_model_state import IChessModelState

class GenomeStockfish:
    """
    Genome for stockfish. Contains parameters for making stockfish bots that will change it's behaviour. 
    """
    def __init__(self, time_constraint : int):
        """
        time_constraint: maximum time of thinking in milliseconds
        """
        if (time_constraint <= 0):
            raise ArgumentError("Time constraint must be above 0")

        self.time_constraint = time_constraint
    
    def crossover(self, other_parent : 'GenomeStockfish') -> 'GenomeStockfish':
        num = randint(0, 1)
        if (num == 0):
            return GenomeStockfish(self.time_constraint)
        else:
            return GenomeStockfish(other_parent.time_constraint)
    
    def mutate(self, mutation_scale : float = 0.1) -> 'GenomeStockfish':
        mutation_num = uniform(1 - mutation_scale, 1 + mutation_scale)
        return GenomeStockfish(round(mutation_num * self.time_constraint))

    @staticmethod
    def create_random() -> 'GenomeStockfish':
        return GenomeStockfish(randint(100, 1000))

    def to_string(self) -> str:
        return "time_constraint: " + str(self.time_constraint)


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
    
    @staticmethod
    def create_from_genome(state: IChessModelState, genome : GenomeStockfish) -> 'BotStockfish':
        return BotStockfish(state, 1000, genome.time_constraint)
    
    def getNextMove(self) -> IMove:
        # Set fen based on model state fen
        self.stockfish.set_fen_position(self.state.getFen())
        
        move = None
        if (self.time_constraint is not None):
            move = str(self.stockfish.get_best_move_time(self.time_constraint))
        else:
            move = str(self.stockfish.get_best_move())
        
        best_move = self.state.stockfishMoveToOurMove(move)
        #print(best_move.getMoveAsString())
        return best_move
    
