import unittest
from piece import Piece
from piece import pieceToValueNorm

class TestPieceImpl(unittest.TestCase):

    def setUp(self):
        self.pawn = Piece.PAWN
        self.queen = Piece.QUEEN
        self.bishop = Piece.BISHOP
        self.knight = Piece.KNIGHT
        self.rook = Piece.ROOK

    def test_pieceToValueNorm(self):
        self.assertEqual(pieceToValueNorm(self.pawn), 0)
        self.assertEqual(pieceToValueNorm(self.queen), 1)
        self.assertEqual(pieceToValueNorm(self.bishop), pieceToValueNorm(self.knight))

    if __name__ == "__main__":
        unittest.main()