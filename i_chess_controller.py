from abc import ABCMeta, abstractmethod
from i_chess_model_state import GameOverStatus


# A player in chess... Could be AI or Human.
class IChessController(metaclass = ABCMeta):

    # Starts the chess game. 
    @abstractmethod
    def run(self) -> GameOverStatus:
        pass