from abc import ABCMeta, abstractmethod
from typing import List
import matplotlib.pyplot as plt

from group_win_data import GroupMatchData

class IFigureGenerator(metaclass = ABCMeta):
    
    # Generate a distribution of total moves made to checkmate.
    @abstractmethod
    def figureOneGen(self):
        pass

    # Generate a distribution of group vs. number of wins
    @abstractmethod
    def figureGroupVWins(self, data : List[GroupMatchData]):
        pass
