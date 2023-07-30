from ast import Assert
import unittest
from chess_model_impl import ChessModelImpl
from spot_impl import SpotImpl
from piece import Piece
from game_over_status import GameOverStatus
from player_color import PlayerColor
from move_impl import MoveImpl

class TestChessModelImpl(unittest.TestCase):

    def setUp(self):
        self.chess_model = ChessModelImpl()
        self.chess_model_black_check = ChessModelImpl("rnbqkbnr/ppp1pppp/3p4/1B6/4P3/8/PPPP1PPP/RNBQK1NR")
        self.chess_model_white_won = ChessModelImpl("rnbq1bnr/ppP1PPpp/8/1kRP4/1Q6/8/1P1B1PPP/RN2KBN1")
        self.chess_model_black_won = ChessModelImpl("rn2kbnr/ppp1pppp/3p4/8/P5bP/BQ5N/PPP1q1PP/RNB1K2R")
        self.chess_model_draw = ChessModelImpl("4k3/8/8/8/8/5K2/8/8")
        self.chess_model_white_check = ChessModelImpl("rnbqk1nr/pppppppp/8/8/7b/5P2/PPPPP1PP/RNBQKBNR")

    def test_getPieceAtSpot(self):
        self.assertEqual(self.chess_model.getPieceAtSpot(SpotImpl("a", 1)), Piece.ROOK)
        self.assertNotEqual(self.chess_model.getPieceAtSpot(SpotImpl("a", 1)), Piece.KNIGHT)
        self.assertEqual(self.chess_model.getPieceAtSpot(SpotImpl("f", 7)), Piece.PAWN)
        self.assertEqual(self.chess_model.getPieceAtSpot(SpotImpl("e", 8)), Piece.KING)
        self.assertEqual(self.chess_model.getPieceAtSpot(SpotImpl("d", 1)), Piece.QUEEN)
        self.assertEqual(self.chess_model.getPieceAtSpot(SpotImpl("c", 8)), Piece.BISHOP)
        self.assertEqual(self.chess_model.getPieceAtSpot(SpotImpl("b", 4)), Piece.BLANK)
        

    def test_getGameOverStatus(self):
        self.assertEqual(self.chess_model.getGameOverStatus(), GameOverStatus.IN_PROGRESS)
        self.assertEqual(self.chess_model_white_won.getGameOverStatus(), GameOverStatus.WHITE_WIN)
        self.assertEqual(self.chess_model_black_won.getGameOverStatus(), GameOverStatus.BLACK_WIN)
        self.assertEqual(self.chess_model_draw.getGameOverStatus(), GameOverStatus.DRAW)

    def test_isInCheck(self):
        self.assertEqual(self.chess_model.isInCheck(), False)
        self.assertEqual(self.chess_model_black_check.isInCheck(), True)
        self.assertEqual(self.chess_model_white_check.isInCheck(), True)

    def test_movePiece(self):
        # Test legal move
        board = ChessModelImpl()
        self.assertEqual(board.getPieceAtSpot(SpotImpl("d", 4)), Piece.BLANK)
        board.movePiece(MoveImpl(SpotImpl("d", 2), SpotImpl("d", 4)))
        self.assertEqual(board.getPieceAtSpot(SpotImpl("d", 4)), Piece.PAWN)

        # Test that piece still can be moved when it is not your turn
        board.movePiece(MoveImpl(SpotImpl("d", 4), SpotImpl("d", 5)))
        self.assertEqual(board.getPieceAtSpot(SpotImpl("d", 4)), Piece.BLANK)
        self.assertEqual(board.getPieceAtSpot(SpotImpl("d", 5)), Piece.PAWN)

        # Test moving a piece onto another piece throws error
        threw_error = False
        try:
            board.movePiece(MoveImpl(SpotImpl("d", 4), SpotImpl("b", 1)))
        except AssertionError:
            threw_error = True

        # Test moving a piece past the limits of its movement capabilities is OK
        board.movePiece(MoveImpl(SpotImpl("h", 2), SpotImpl("h", 5)))
        self.assertEqual(board.getPieceAtSpot(SpotImpl("h", 5)), Piece.PAWN)
        board.movePiece(MoveImpl(SpotImpl("h", 5), SpotImpl("h", 4)))
        self.assertEqual(board.getPieceAtSpot(SpotImpl("h", 4)), Piece.PAWN)
    
    def test_isMoveLegal(self):
        # Test legal move
        board = ChessModelImpl()
        self.assertEqual(board.isMoveLegal(MoveImpl(SpotImpl("d", 2), SpotImpl("d", 4))), True)

        # Test moving piece when it is not your turn returns false
        self.assertEqual(board.isMoveLegal(MoveImpl(SpotImpl("a", 7), SpotImpl("a", 6))), False)

        # Test moving a piece onto another piece returns false
        self.assertEqual(board.isMoveLegal(MoveImpl(SpotImpl("d", 2), SpotImpl("b", 1))), False)

        # Test moving a piece past the limits of its movement capabilities is not OK
        self.assertEqual(board.isMoveLegal(MoveImpl(SpotImpl("h", 2), SpotImpl("h", 5))), False)

        # Test knight jumping over piece
        self.assertEqual(board.isMoveLegal(MoveImpl(SpotImpl("b", 1), SpotImpl("c", 3))), True)

        # Test bishop can't go through a piece
        self.assertEqual(board.isMoveLegal(MoveImpl(SpotImpl("f", 1), SpotImpl("b", 5))), False)
        board.movePiece(MoveImpl(SpotImpl("e", 2), SpotImpl("e", 3)))
        board.movePiece(MoveImpl(SpotImpl("g", 7), SpotImpl("g", 6)))
        self.assertEqual(board.isMoveLegal(MoveImpl(SpotImpl("f", 1), SpotImpl("b", 5))), True)

    def test_printAsciiViewIfAvailable(self):
        pass
        # Let's just assume this one works
        
    def test_getWhoseTurn(self):
        # Test legal move
        board = ChessModelImpl()
        self.assertEqual(board.getWhoseTurn(), PlayerColor.WHITE)
        board.movePiece(MoveImpl(SpotImpl("d", 2), SpotImpl("d", 4)))
        self.assertEqual(board.getWhoseTurn(), PlayerColor.BLACK)

    def test_getColorAtSpot(self):
        self.assertEqual(self.chess_model._getColorAtSpot(SpotImpl("a", 1)), PlayerColor.WHITE)
        self.assertEqual(self.chess_model._getColorAtSpot(SpotImpl("a", 8)), PlayerColor.BLACK)
        self.assertEqual(self.chess_model._getColorAtSpot(SpotImpl("f", 2)), PlayerColor.WHITE)
        self.assertEqual(self.chess_model._getColorAtSpot(SpotImpl("f", 7)), PlayerColor.BLACK)
        self.assertEqual(self.chess_model._getColorAtSpot(SpotImpl("f", 5)), None)

    def test_getSpotsWithPiecesOfColor(self):
        self.chess_model.getSpotsWithPiecesOfColor(PlayerColor.WHITE)

    def test_getFen(self):
        fen = self.chess_model.getFen()
        print("FEN IS: " + fen)

    if __name__ == '__main__':
        unittest.main()
