import unittest
from spot_impl import SpotImpl
from i_human_player_impl import HumanPlayerImpl
from chess_model_impl import ChessModelImpl
from i_chess_model_state import IChessModelState
from ast import Assert

class TestSpotImpl(unittest.TestCase):
    pass
    # def setUp(self):
    #     self.chessModel = ChessModelImpl()
    #     self.player1 = HumanPlayerImpl(self.chessModel)
    #     self.player2 = HumanPlayerImpl(self.chessModel)

    # def testGetNextMove_0(self):
    #     print("\n")
    #     move = self.player1.getNextMove()
    #     self.assertEqual(move.getMoveAsString(), "a2a8")
    #     self.assertEqual(move.getPromotionTypeIfAvailable().name, "KING")

    # def testGetNextMove_1(self):
    #     print("\n")
    #     move = self.player1.getNextMove()
    #     self.assertEqual(move.getMoveAsString(), "b2b1")
    #     self.assertEqual(move.getPromotionTypeIfAvailable().name, "ROOK")