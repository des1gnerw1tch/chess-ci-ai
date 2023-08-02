from abc import ABCMeta, abstractmethod
from game_over_status import GameOverStatus


# A player in chess... Could be AI or Human.
class IChessController(metaclass = ABCMeta):

    # Starts the chess game. 
    @abstractmethod
    def run(self) -> GameOverStatus:
        pass
    
    # Store total moves
    @abstractmethod
    def getTotalMoves(self) -> int:
        pass