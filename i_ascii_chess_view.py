from abc import ABCMeta, abstractmethod
from typing import List

# player view of chess game
class IAsciiChessView(metaclass = ABCMeta):
    @abstractmethod
    def printBoard(self, state):
        pass

    @abstractmethod
    def printValidMoves(self):
        pass

    # @abstractmethod
    # def printWinScreen():
    #     pass

    # @abstractmethod
    # def printErrorMessage():
    #     pass