"""
Some re-used functionality that bots share. 
"""

from i_chess_model_state import IChessModelState
from i_move import IMove
from i_spot import ISpot
from random import randint
from piece import Piece, pieceToValue
from typing import Union, List


def getRandomSpotToMoveFrom(state: IChessModelState) -> ISpot:
    """
    Returns a random spot, where that spot has at least one valid move in currrent board state.
    """
    listOfMoves = state.getValidMoves()
    listOfSpotsWhereCanMove = []

    # TODO: Look at this next session contains might be shallow
    for move in listOfMoves:
        if (not listOfSpotsWhereCanMove.__contains__(move.getLocation())):
            listOfSpotsWhereCanMove.append(move.getLocation())
    
    spot : ISpot = listOfSpotsWhereCanMove[randint(0, len(listOfSpotsWhereCanMove) - 1)]
    return spot

# TODO: Debug statements are commented out, create better system for debug stuff
def getMovesFromSpot(state: IChessModelState, spot: ISpot) -> Union[List[IMove], None]:
    """
    Gets all valid moves from a given spot location. 
    """
    listOfMoves = state.getValidMoves()
    movesFromSpot = []

    for move in listOfMoves:
        if (spot.equals(move.getLocation())):
            movesFromSpot.append(move)
    #for move in movesFromSpot:
        #print("Moves from spot: " + move.getMoveAsString())
    
    return movesFromSpot


# TODO: Debug statements are commented out, create better system for debug stuff
def getHighestCaptureMove(state: IChessModelState, spot : ISpot) -> Union[IMove, None]:
    """
    Returns a Move from a spot that captures the greatest value piece. If there is no capturing move available, 
    will return None. If two moves provide a capture of the same value, will return a random one.
    state: Model state of the chess game
    spot: Spot to move from
    """
    movesFromSpot = getMovesFromSpot(state, spot)

    captureMoves = []
    for move in movesFromSpot:
        if (state.getPieceAtSpot(move.getDestination()) != Piece.BLANK):
            captureMoves.append(move)
    #for move in captureMoves:
        #print("Capture moves: " + move.getMoveAsString())
    
    maxCapturePieceValue = 0
    for move in captureMoves:
        if (pieceToValue(state.getPieceAtSpot(move.getDestination())) > maxCapturePieceValue):
            maxCapturePieceValue = pieceToValue(state.getPieceAtSpot(move.getDestination()))

    maxCaptureMoves = []
    for move in captureMoves:
        if (pieceToValue(state.getPieceAtSpot(move.getDestination())) == maxCapturePieceValue):
            maxCaptureMoves.append(move)

    if (len(maxCaptureMoves) > 0):
        result = maxCaptureMoves[randint(0, len(maxCaptureMoves) - 1)]
        return result
    else:
        return None

