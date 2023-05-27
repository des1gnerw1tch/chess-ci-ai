from chess_model_impl import ChessModelImpl
from i_ascii_chess_view_impl import IAsciiChessViewImpl
from ai_random_moves_player import AIRandomMovesPlayer
from chess_controller_impl import ChessControllerImpl
from game_over_status import GameOverStatus
from i_human_player_impl import HumanPlayerImpl

def makeGame():
    model = ChessModelImpl()
    view = IAsciiChessViewImpl(model)
    player1 = AIRandomMovesPlayer(model)
    player2 = HumanPlayerImpl(model)
    return ChessControllerImpl(model, view, player1, player2)

if __name__ == '__main__':
    win = False
    i = 0
    while(not win):
        i += 1
        win = makeGame().run() != GameOverStatus.DRAW
    
    print("Game till a win: " + str(i))
    
