from enum import Enum

class Piece(Enum):
    BLANK = 0
    PAWN = 1
    ROOK = 2
    KNIGHT = 3
    BISHOP = 4
    QUEEN = 5
    KING = 6

def pieceToValue(piece : Piece):
    if (piece is Piece.PAWN):
        return 1
    if (piece is Piece.ROOK):
        return 5
    if (piece is Piece.KNIGHT):
        return 3
    if (piece is Piece.BISHOP):
        return 3
    if (piece is Piece.QUEEN):
        return 9
    if (piece is Piece.KING):
        raise ValueError('King has no assigned value')