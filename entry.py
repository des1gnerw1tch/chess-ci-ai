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
from bot_stockfish import BotStockfish


def makeGame():
    model = ChessModelImpl()
    view = IAsciiChessViewImpl(model)
    white_player = BotCI2(model, 2, 1, 1000)
    black_player = BotStockfish(model, 0, 10)
    #white_player = AIRandomMovesPlayer(model)
    return ChessControllerImpl(model, view, white_player, black_player)


def gameTillWin(): 
    win = False
    i = 0
    while(not win):
        i += 1
        win = makeGame().run() != GameOverStatus.DRAW
    
    print("Game till a win: " + str(i))

def makeFigure(figure : int):
    total_moves = makeGame().getTotalMoves()
    figureGen = FigureGeneratorImpl()

    if (figure == 1):
        figureGen.figureOneGen(total_moves)
    elif (figure == 2):
        print("CALLING NONEXISTENT FIGURE")
    
def playMatches(matches : int):
    draws = 0
    white_wins = 0
    black_wins = 0
    for i in range(matches):
        result = makeGame().run()
        if (result == GameOverStatus.DRAW):
            draws += 1
        elif (result == GameOverStatus.WHITE_WIN):
            white_wins += 1
        elif (result == GameOverStatus.BLACK_WIN):
            black_wins += 1
    
    print("White wins: " + str(white_wins))
    print("Black wins: " + str(black_wins))
    print ("Draws: " + str(draws))
    makeFigure(1)

if __name__ == '__main__':
    playMatches(1)