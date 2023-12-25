from chess_model_impl import ChessModelImpl
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

if __name__ == '__main__':
    playMatches(1000)
