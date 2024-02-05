import matplotlib.pyplot as plt
import numpy as np
from chess_controller_impl import ChessControllerImpl
from i_chess_model import IChessModel
from i_chess_model_state import IChessModelState
from i_figure_generator import IFigureGenerator
from group_win_data import GroupMatchData
from typing import List
import time

class FigureGeneratorImpl(IFigureGenerator):

    # Generate a histogram distribution of total moves made to checkmate.
    def figureOneGen(self, total_moves_list):
        data = total_moves_list

        # Create the histogram
        plt.hist(data, bins=len(total_moves_list), edgecolor='black')

        # Add labels and title
        plt.title("BotStockfish(ELO 4000) vs BotStockfish(ELO 0): 10 matches", pad=20)
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
    
    def figureGroupVWins(self, data: List[GroupMatchData]):
        # Get data for all groups
        x : List[int] = [] # X-axis values
        wins : List[int] = []
        losses : List[int] = []
        draws : List[int] = []
        for e in data:
            x.append(e.number)
            wins.append(e.wins)
            losses.append(e.losses)
            draws.append(e.draws)

        # Get name of opponent (assuming all groups face the same opponent)
        x_label = data[0].number_label
        opponent_name = data[0].opponent
    

        y1 = wins  # Y-axis values for first line
        y2 = losses # Y-axis values for second line
        y3 = draws  # Y-axis values for third line

        # Plotting the lines
        plt.plot(x, y1, marker='o', linestyle='-', color='g', label='Wins')  # Plotting the first line
        plt.plot(x, y2, marker='o', linestyle='-', color='r', label='Losses')  # Plotting the second line
        plt.plot(x, y3, marker='o', linestyle='-', color='#8b4513', label='Draws')  # Plotting the third line
        plt.xlabel(x_label)
        plt.ylabel('Wins, Losses, Draws')
        plt.title("Wins, Losses, Draws of" + " vs. " + x_label)
        plt.suptitle('vs. ' + opponent_name, fontsize=12, color='blue')
        plt.legend()  # Show legend based on label

        # Display the plot
        plt.grid(True)  # Show grid
        plt.savefig("fig" + str(time.time()) + ".png")

    