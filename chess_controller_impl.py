from pyexpat import model
from i_chess_controller import IChessController
from i_chess_model import IChessModel
from i_chess_model_state import GameOverStatus, PlayerColor
from i_player import IPlayer

class ChessControllerImpl(IChessController):
    model : IChessModel = None
    view = None
    white_player : IPlayer = None
    black_player : IPlayer = None

    def __init__(self, model : IChessModel, view, white_player : IPlayer, black_player : IPlayer):
        self.model = model
        self.view = view
        self.white_player = white_player
        self.black_player = black_player

    #TODO: Test and add IView support
    def run(self) -> GameOverStatus:

        while(self.model.getGameOverStatus() == GameOverStatus.IN_PROGRESS):
            # view.printBoard()
            move = None
            if (self.model.getWhoseTurn() == PlayerColor.WHITE):
                print("White players turn, what will be your move...")
                move = self.white_player.getNextMove()
            else:
                print ("Black players turn, what will be your move...")
                move = self.black_player.getNextMove()
            
            if (self.model.isMoveLegal(move)):
                self.model.movePiece(move)
            else:
                print("Move not valid.")

        print("Game over. Result: " + self.model.getGameOverStatus())
        return self.model.getGameOverStatus()


            
