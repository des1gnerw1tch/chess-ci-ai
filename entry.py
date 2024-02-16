from chess_model_impl import ChessModelImpl
from group_win_data import GroupMatchData
from i_ascii_chess_view_impl import IAsciiChessViewImpl
from ai_random_moves_player import AIRandomMovesPlayer
from chess_controller_impl import ChessControllerImpl
from game_over_status import GameOverStatus
from i_human_player_impl import HumanPlayerImpl
from i_figure_generator_impl import FigureGeneratorImpl
from bot_ci_0 import BotCI0
from bot_ci_1 import BotCI1
from bot_ci_2 import BotCI2
from bot_ci_3 import BotCI3
from bot_stockfish import BotStockfish
from typing import List

def makeGame():
    model = ChessModelImpl()
    view = IAsciiChessViewImpl(model)
    white_player = BotCI3(model, 2, 1, 1000, 0.75)
    black_player = BotCI1(model)
    #black_player = AIRandomMovesPlayer(model)
    #white_player = AIRandomMovesPlayer(model)
    return ChessControllerImpl(model, view, white_player, black_player)


def gameTillWin(): 
    win = False
    i = 0
    while(not win):
        i += 1
        win = makeGame().run() != GameOverStatus.DRAW
    
    print("Game till a win: " + str(i))

def makeFigure(figure : int, total_moves_list : list):
    figureGen = FigureGeneratorImpl()

    if (figure == 1):
        figureGen.figureOneGen(total_moves_list)
    elif (figure == 2):
        print("CALLING NONEXISTENT FIGURE")
    
def playMatches(matches : int):
    draws = 0
    white_wins = 0
    black_wins = 0
    total_moves_list = list()

    for i in range(matches):
        print("\n\n ======GAME NUMBER " + str(i) + "==========\n\n")
        controller = makeGame()
        result = controller.run()
        if (result == GameOverStatus.DRAW):
            draws += 1
        elif (result == GameOverStatus.WHITE_WIN):
            white_wins += 1
        elif (result == GameOverStatus.BLACK_WIN):
            black_wins += 1
    
        total_moves = controller.getTotalMoves()
        print("TOTAL MOVES IS: " + str(total_moves))
        total_moves_list.append(total_moves)

    print("White wins: " + str(white_wins))
    print("Black wins: " + str(black_wins))
    print ("Draws: " + str(draws))
    makeFigure(1, total_moves_list)

def testStockfishELO():
    f = FigureGeneratorImpl()
    elo = 0
    d : List[GroupMatchData] = []
    # For ELO's 0 to 1800
    for i in range(0, 10):
        print("==============")
        print("ELO: " + str(elo))
        print("==============")
        draws = 0
        stockfish_losses = 0
        stockfish_wins = 0
        # Play X games each
        for j in range (0, 5):
            model = ChessModelImpl()
            view = IAsciiChessViewImpl(model)
            white_player = BotStockfish(model, 500)
            black_player = BotStockfish(model, elo)
            result = ChessControllerImpl(model, view, white_player, black_player).run()
            if (result == GameOverStatus.DRAW):
                draws += 1
            elif (result == GameOverStatus.WHITE_WIN):
                stockfish_losses += 1
            elif (result == GameOverStatus.BLACK_WIN):
                stockfish_wins += 1
        d.append(GroupMatchData(elo, "Stockfish ELO", "Stockish ELO: 500", stockfish_wins, draws, stockfish_losses))
        elo+= 200

    f.figureGroupVWins(d)

def testStockfishTimeConstraint():
    f = FigureGeneratorImpl()
    time_constraint = 0
    d : List[GroupMatchData] = []
    # For Time constraint 0 to 1000 milliseconds
    for i in range(0, 6):
        print("==============")
        print("Time Constraint: " + str(time_constraint))
        print("==============")
        draws = 0
        stockfish_losses = 0
        stockfish_wins = 0
        # Play X games each
        for j in range (0, 10):
            model = ChessModelImpl()
            view = IAsciiChessViewImpl(model)
            white_player = BotStockfish(model, 1000, 500)
            black_player = BotStockfish(model, 1000, time_constraint)
            result = ChessControllerImpl(model, view, white_player, black_player).run()
            if (result == GameOverStatus.DRAW):
                draws += 1
            elif (result == GameOverStatus.WHITE_WIN):
                stockfish_losses += 1
            elif (result == GameOverStatus.BLACK_WIN):
                stockfish_wins += 1
        d.append(GroupMatchData(time_constraint, "Stockfish ELO 1000, time_constraint", "Stockish ELO 1000, time_constraint: 500", stockfish_wins, draws, stockfish_losses))
        time_constraint+= 200

    f.figureGroupVWins(d)

def testChanceGoForKingEffectsResults():
    f = FigureGeneratorImpl()
    chance = 0
    d : List[GroupMatchData] = []
    # For chances 0 to 1, increments of 1/20
    for i in range(0, 21):
        print("==============")
        print("Chance go for king : " + str(chance))
        print("==============")
        draws = 0
        losses = 0
        wins = 0
        # Play 100 games each
        for i in range (0, 100):
            model = ChessModelImpl()
            view = IAsciiChessViewImpl(model)
            white_player = AIRandomMovesPlayer(model)
            black_player = BotCI3(model, 1, 1, 10000, chance, False)
            result = ChessControllerImpl(model, view, white_player, black_player).run()
            if (result == GameOverStatus.DRAW):
                draws += 1
            elif (result == GameOverStatus.WHITE_WIN):
                losses += 1
            elif (result == GameOverStatus.BLACK_WIN):
                wins += 1
        d.append(GroupMatchData(chance, "BotCI3 chance go for king", "AIRandomMovesPlayer", wins, draws, losses))
        chance+= 1/20
        chance = round(chance, 2)

    f.figureGroupVWins(d)

if __name__ == '__main__':
    #testStockfishELO()
    testStockfishTimeConstraint()
    #testChanceGoForKingEffectsResults()
    #playMatches(1000)
