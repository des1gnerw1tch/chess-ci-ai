import random
from i_player import IPlayer
from i_move import IMove
from i_chess_model_state import IChessModelState
from i_spot import ISpot
from piece import Piece, pieceToValue

# An AI player where will choose a random piece to move, and that piece will try to capture 
# the maximum value piece
class BotCI1(IPlayer):
    state : IChessModelState

    def __init__(self, state : IChessModelState) -> None:
        self.state = state

    def getNextMove(self) -> IMove:
        listOfMoves = self.state.getValidMoves()

        listOfSpotsWhereCanMove = []

        # TODO: Look at this next session contains might be shallow
        for move in listOfMoves:
            if (not listOfSpotsWhereCanMove.__contains__(move.getLocation())):
                listOfSpotsWhereCanMove.append(move.getLocation())
        
        spot : ISpot = listOfSpotsWhereCanMove[random.randint(0, len(listOfSpotsWhereCanMove) - 1)]
        print("Spot chosen by Bot 1: " + spot.getSpotAsString())
        movesFromSpot = []
        
        for move in listOfMoves:
            if (spot.equals(move.getLocation())):
                movesFromSpot.append(move)
        for move in movesFromSpot:
            print("Moves from spot: " + move.getMoveAsString())

        captureMoves = []
        for move in movesFromSpot:
            if (self.state.getPieceAtSpot(move.getDestination()) != Piece.BLANK):
                captureMoves.append(move)
        for move in captureMoves:
            print("Capture moves: " + move.getMoveAsString())
        
        maxCapturePieceValue = 0
        for move in captureMoves:
            if (pieceToValue(self.state.getPieceAtSpot(move.getDestination())) > maxCapturePieceValue):
                maxCapturePieceValue = pieceToValue(self.state.getPieceAtSpot(move.getDestination()))

        maxCaptureMoves = []
        for move in captureMoves:
            if (pieceToValue(self.state.getPieceAtSpot(move.getDestination())) == maxCapturePieceValue):
                maxCaptureMoves.append(move)

        if (len(maxCaptureMoves) > 0):
            result = maxCaptureMoves[random.randint(0, len(maxCaptureMoves) - 1)]
            print("Max capture move selected")
        else:
            result = movesFromSpot[random.randint(0, len(movesFromSpot) - 1)]
            print("Non capture move selected")
        print("Move chosen by Bot 1: " + result.getMoveAsString())
        return result