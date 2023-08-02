from abc import ABCMeta, abstractmethod
import matplotlib.pyplot as plt

class IFigureGenerator(metaclass = ABCMeta):
    
    # Generate a distribution of total moves made to checkmate.
    @abstractmethod
    def figureOneGen(self):
        pass