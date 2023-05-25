from argparse import ArgumentError
from i_chess_model import IChessModel
from i_spot import ISpot
from game_over_status import GameOverStatus
from piece import Piece
from player_color import PlayerColor
from i_move import IMove
from move_impl import MoveImpl
from spot_impl import SpotImpl
from typing import List
from chess import Board, Move, WHITE, BLACK, Square, parse_square, PieceType, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING

# This model implements chess with the "chess" python module. A great descriptive name
# for a chess module!
class ChessModelImpl(IChessModel):
    chess_board = None

    # FEN is string for starting board
    def __init__(self, fen : str = None):
        if (fen is None):
            self.chess_board = Board()
        else:
            self.chess_board = Board(fen)

    def getPieceAtSpot(self, spot: ISpot) -> Piece:
        square = self.__iSpotToSquare(spot)
        piece = self.chess_board.piece_at(square)
        if (piece is None):
            return Piece.BLANK
        
        pieceStr = piece.symbol().lower()

        if (pieceStr == "p"):
            return Piece.PAWN
        elif (pieceStr ==  "r"):
            return Piece.ROOK
        elif (pieceStr == "k"):
            return Piece.KING
        elif (pieceStr == "n"):
            return Piece.KNIGHT
        elif (pieceStr == "q"):
            return Piece.QUEEN
        elif (pieceStr == "b"):
            return Piece.BISHOP
        else:
            raise ValueError("pieceStr has unknown value")

    def getValidMoves(self) -> List[IMove]:
        legalMoves = list(self.chess_board.legal_moves)

        myLegalMoves = list()

        for move in legalMoves:
            fromSpot = SpotImpl((move.uci())[0], int((move.uci())[1]))
            toSpot = SpotImpl((move.uci())[2], int((move.uci())[3]))

            myMove = MoveImpl(fromSpot, toSpot, self.__theirPieceToOurPiece(move.promotion))

            myLegalMoves.append(myMove)

        return myLegalMoves

    def getGameOverStatus(self) -> GameOverStatus:
        white_turn_board = self.chess_board.copy()
        white_turn_board.turn = WHITE
        outcome_white = white_turn_board.outcome()

        black_turn_board = self.chess_board.copy()
        black_turn_board.turn = BLACK
        outcome_black = black_turn_board.outcome()

        if outcome_white is None and outcome_black is None:
            return GameOverStatus.IN_PROGRESS

        if (outcome_white is not None):
            color = outcome_white.winner
        else:
            color = outcome_black.winner

        if color == WHITE:
            return GameOverStatus.WHITE_WIN
        elif color == BLACK:
            return GameOverStatus.BLACK_WIN
        elif color is None:
            return GameOverStatus.DRAW

    def isInCheck(self) -> bool:
        board_copy = self.chess_board.copy()
        board_copy2 = self.chess_board.copy()
        board_copy.turn = WHITE
        board_copy2.turn = BLACK
        return board_copy.is_check() or board_copy2.is_check()

    def movePiece(self, move: IMove) -> None:
        move = self.__iMoveToMove(move)
        self.chess_board.push(move)
    
    def isMoveLegal(self, move: IMove):
        move = self.__iMoveToMove(move)
        return move in self.chess_board.legal_moves

    def printAsciiViewIfAvailable(self) -> str:
        return str(self.chess_board)

    # TODO: Test
    def getWhoseTurn(self) -> PlayerColor:
        if self.chess_board.turn == WHITE:
            return PlayerColor.WHITE
        else:
            return PlayerColor.BLACK

    # Returns the chess.Square index of the ISpot to be used by this chess module
    def __iSpotToSquare(self, spot: ISpot) -> Square:
        name = spot.getCol() + spot.getRow()
        return parse_square(name)

    def __iMoveToMove(self, i_move : IMove):
        return Move(self.__iSpotToSquare(i_move.getLocation()), 
        self.__iSpotToSquare(i_move.getDestination()), 
        self.__ourPieceToTheirPiece(i_move.getPromotionTypeIfAvailable()))

    # Translates our Piece type to the chess modules PieceType type
    def __ourPieceToTheirPiece(self, piece : Piece) -> PieceType:
        if (piece == Piece.BISHOP):
            return BISHOP
        elif (piece == Piece.KING):
            return KING
        elif (piece == Piece.PAWN):
            return PAWN
        elif (piece == Piece.ROOK):
            return ROOK
        elif (piece == Piece.QUEEN):
            return QUEEN
        elif (piece == Piece.KNIGHT):
            return KNIGHT
        return None

    # Translates their PieceType type our Piece type
    def __theirPieceToOurPiece(self, piece : PieceType) -> Piece:
        if (piece == BISHOP):
            return Piece.BISHOP
        elif (piece == KING):
            return Piece.KING
        elif (piece == PAWN):
            return Piece.PAWN
        elif (piece == ROOK):
            return Piece.ROOK
        elif (piece == QUEEN):
            return Piece.QUEEN
        elif (piece == KNIGHT):
            return Piece.KNIGHT
        return None