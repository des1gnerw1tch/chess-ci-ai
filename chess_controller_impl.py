from i_chess_controller import IChessController
from i_chess_model import IChessModel
from game_over_status import GameOverStatus
from player_color import PlayerColor
from i_player import IPlayer
from i_ascii_chess_view import IAsciiChessView
from i_figure_generator import IFigureGenerator

class ChessControllerImpl(IChessController):
    model : IChessModel = None
    view: IAsciiChessView = None 
    white_player : IPlayer = None
    black_player : IPlayer = None

    def __init__(self, model : IChessModel, view : IAsciiChessView, white_player : IPlayer, black_player : IPlayer):
        self.model = model
        self.view = view
        self.white_player = white_player
        self.black_player = black_player

    #TODO: Test
    def run(self, show_debug = True) -> GameOverStatus:
        while(self.model.getGameOverStatus() == GameOverStatus.IN_PROGRESS):
            if (show_debug):
                print("Fen: " + self.model.getFen())
                self.view.printBoard()
            move = None
            if (self.model.getWhoseTurn() == PlayerColor.WHITE):
                if (show_debug):
                    print("White players turn, what will be your move...")
                move = self.white_player.getNextMove()
            else:
                if (show_debug):
                    print ("Black players turn, what will be your move...")
                move = self.black_player.getNextMove()
            
            if (self.model.isMoveLegal(move)):
                self.model.movePiece(move)
            else:
                if (show_debug):
                    print("Move not valid.")

        if (show_debug):
            print("Game over. Result: " + str(self.model.getGameOverStatus()))
            print("Total moves to checkmate: " + str(self.model.getTotalMoves()))

        self.view.printBoard()
        return self.model.getGameOverStatus()

    # Store total moves
    def getTotalMoves(self) -> int:
        return self.model.getTotalMoves()
            
