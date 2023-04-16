from abc import ABCMeta, abstractmethod


# A player in chess... Could be AI or Human.
class IChessController(metaclass = ABCMeta):

    # Starts the chess game. 
    @abstractmethod
    def run() -> None:
        pass