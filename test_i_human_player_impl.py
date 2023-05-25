import unittest
from spot_impl import SpotImpl
from i_human_player_impl import HumanPlayerImpl
from chess_model_impl import ChessModelImpl
from i_chess_model_state import IChessModelState

class TestSpotImpl(unittest.TestCase):

    def setUp(self):
        self.chessModel = ChessModelImpl()
        self.chessModelState = IChessModelState()
        self.player1 = HumanPlayerImpl()
        self.player2 = HumanPlayerImpl()

    def testGetNextMove(self):
        print("\n")
        move = self.player1.getNextMove(self.chessModelState)
        print(move.getMoveAsString())