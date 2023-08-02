import matplotlib.pyplot as plt
import numpy as np
from chess_controller_impl import ChessControllerImpl
from i_chess_model import IChessModel
from i_chess_model_state import IChessModelState
from i_figure_generator import IFigureGenerator


class FigureGeneratorImpl(IFigureGenerator):

    # Generate a distribution of total moves made to checkmate.
    def figureOneGen(self, total_moves_list):
        data = total_moves_list

        # Create the histogram
        plt.hist(data, bins=len(total_moves_list), edgecolor='black')

        # Add labels and title
        # plt.title("Histogram Example")
        plt.xlabel("Total moves")
        plt.ylabel("Games")
        plt.legend()
        mean_value = np.mean(data)
        plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_value:.2f}')
        std_deviation = np.std(data)
        plt.axvline(mean_value + std_deviation, color='green', linestyle='dashed', linewidth=2, label=f'Std Dev: {std_deviation:.2f}')
        plt.axvline(mean_value - std_deviation, color='green', linestyle='dashed', linewidth=2)
        plt.text(mean_value, plt.ylim()[1], f'Mean: {mean_value:.2f}', color='red', ha='center', va='bottom')
        plt.text(mean_value + std_deviation, plt.ylim()[1], f'Std Dev: {std_deviation:.2f}', color='green', ha='center', va='bottom')
        plt.text(mean_value - std_deviation, plt.ylim()[1], f'Std Dev: {std_deviation:.2f}', color='green', ha='center', va='bottom')

        # Display the plot
        plt.show()
    