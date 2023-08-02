import matplotlib.pyplot as plt
from chess_controller_impl import ChessControllerImpl
from i_figure_generator import IFigureGenerator


class FigureGeneratorImpl(IFigureGenerator):
    def __init__(self):
        pass
    
    # Generate a distribution of total moves made to checkmate.
    def figureOneGen(self, total_moves):
        print("FIGURE GEN ONE CALLED!!")
        return total_moves