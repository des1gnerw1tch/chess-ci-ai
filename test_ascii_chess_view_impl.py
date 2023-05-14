import unittest
from spot_impl import SpotImpl
from i_ascii_chess_view_impl import IAsciiChessViewImpl
from chess_model_impl import ChessModelImpl
from i_chess_model_state import IChessModelState

class TestSpotImpl(unittest.TestCase):

    def setUp(self):
        self.validConstruct1 = SpotImpl("a", 1)
        self.validConstruct2 = SpotImpl("b", 3)
        self.chessModel = ChessModelImpl()
        self.AsciiView = IAsciiChessViewImpl(self.chessModel)

    def testPrintSpotAsString(self):
        self.assertEqual(self.validConstruct1.getSpotAsString(), "a1")
        self.assertEqual(self.validConstruct2.getSpotAsString(), "b3")

    # test getValidMoves from chess model
    def testGetValidMoves(self):
        print(self.chessModel.getValidMoves())

    # test printValidMoves from ascii chess view
    def testPrintValidMoves(self):
        self.AsciiView.printValidMoves()
    
    if __name__ == '__main__':
        unittest.main()