from argparse import ArgumentError
from i_player import IPlayer
from i_move import IMove
from i_chess_model_state import IChessModelState
from i_spot import ISpot
from piece import Piece, pieceToValueNorm
from bot_utils import getRandomSpotToMoveFrom, getHighestCaptureMove, getMovesFromSpot
from player_color import PlayerColor
from typing import List
from random import randint, random

class BotCI3(IPlayer):
    """
    An AI player where will choose a random piece to move, and that piece will try to capture 
    the maximum value piece. If that piece can't find a capture, it will move closer to a 
    piece depending on weights of a couple factors.

    Builds on BotCI2 by allowing pieces to go for the king more often. The pieces will go for the 
    king based on a given chance (chanceForKing) when there are no capturing moves. 
    """
    def __init__(self, state : IChessModelState, proximityWeight: float, pieceValueWeight: float,
                maxProximityDistance: float, chanceGoForKing: float) -> None:
        """
        state: Chess board
        proximityWeight: How much to favor closer pieces when choosing a piece to approach.
        pieceValueWeight: How much to favor piece value when choosing a piece to approach.
        maxProximityDistance: The max distance (in squares) a piece can be away to be considered.
        """
        self.state = state
        self.proximityWeight = proximityWeight
        self.pieceValueWeight = pieceValueWeight
        self.maxProximityDistance = maxProximityDistance

        if (chanceGoForKing > 1 or chanceGoForKing < 0):
            raise ArgumentError("Chance go for king has to be between 0-1")
        
        self.chanceGoForKing = chanceGoForKing


    def getNextMove(self) -> IMove:
        spot = getRandomSpotToMoveFrom(self.state)
        maxCaptureMove = getHighestCaptureMove(self.state, spot)
        if maxCaptureMove is None:
            spotToApproach = self._getSpotToApproach(spot)
            move = self._approachSpot(spot, spotToApproach)
            print("Non capture move selected")
            result = move
        else:
            result = maxCaptureMove
        print("Move chosen by Bot 3: " + result.getMoveAsString())
        return result
    

    def _getSpotToApproach(self, attackingSpot : ISpot) -> ISpot:
        """
        Returns a spot to approach, weighting in factors such as how close is piece to approach,
        and what is the piece value of piece to approach. Uses a score, where the higher score
        represents a higher desire to go for that piece. If there is more than one high score,
        will choose a random piece to attack from them. Pieces will not follow King unless it is
        the last piece on the board. 
        attackingSpot: The spot of the piece that will do the approaching
        """
        if (self.state.getWhoseTurn() == PlayerColor.BLACK):
            enemyColor = PlayerColor.WHITE
        else:
            enemyColor = PlayerColor.BLACK

        enemySpots = self.state.getSpotsWithPiecesOfColor(enemyColor)

        print("Spots with color list length: " + str(len(enemySpots)))
        enemySpotAndScore = {}

        # Get the scores for each enemy spot. High score indicates more want to approach.
        # Don't score any enemy spot that is not within reach of proximity (maxProximityDistance)
        kingSpot = None
        for enemySpot in enemySpots:
            if attackingSpot.distanceTo(enemySpot) > self.maxProximityDistance:
                continue
            elif self.state.getPieceAtSpot(enemySpot) == Piece.KING: # Will not follow king
                kingSpot = enemySpot
                continue
            enemySpotAndScore[enemySpot] = self._calculateSpotScore(attackingSpot, enemySpot)
        

        highestScoringEnemySpots : List[ISpot] = []
        highestScore : float = float('-inf')
        tolerance = 1e-9
        for spot in enemySpotAndScore:
            score = enemySpotAndScore[spot]
            if (abs(score - highestScore) < tolerance):
                highestScoringEnemySpots.append(spot)
            elif (score > highestScore):
                highestScoringEnemySpots.clear()
                highestScore = score
                highestScoringEnemySpots.append(spot)

        if (len(highestScoringEnemySpots) == 0):
            print("No pieces left to follow! Now will check if king is visible")
            if (kingSpot is None):
                print("No kings are visible. Will choose a random spot to move to.")
                randMoves = getMovesFromSpot(self.state, attackingSpot)
                return randMoves[randint(0, len(randMoves) - 1)].getDestination()
            else:
                print("Moving towards king!")
                return kingSpot
            
        # Decide if want to go for king or to go for highest scoring enemy spot, dependent on probablility
        r = random()
        print("Chance go for king: " + str(self.chanceGoForKing) + " float chosen: " + str(r))
        if (r < self.chanceGoForKing):
            print("Going for king!")
            return kingSpot
        else:
            print("Going for highest scoring enemy spot/s")
            return highestScoringEnemySpots[randint(0, len(highestScoringEnemySpots) - 1)]


    def _calculateSpotScore(self, locationOfAttackingPiece : ISpot, enemySpot : ISpot) -> float:
        proximityScore = locationOfAttackingPiece.distanceToNorm(enemySpot) * self.proximityWeight
        pieceValueScore = pieceToValueNorm(self.state.getPieceAtSpot(enemySpot)) * self.pieceValueWeight

        print("Spot being scored: " + enemySpot.getSpotAsString() + " Piece Type: " + str(self.state.getPieceAtSpot(enemySpot)) + 
        " Proximity Score: " + str(proximityScore) + " Piece value score: " + str(pieceValueScore) + " Total Score: " + str(proximityScore + pieceValueScore))

        return proximityScore + pieceValueScore

    
    def _approachSpot(self, fromSpot : ISpot, approachSpot : ISpot) -> IMove:
        """
        Returns a move that gets the from moving piece closest to the piece to approach.
        If there are two closest moves, will choose a random one from them.  
        fromSpot: Spot of the moving piece
        approachSpot: Spot of the piece to approach
        """
        moves : List[IMove] = getMovesFromSpot(self.state, fromSpot)
        movesClosestToApproachSpot : List[IMove]= []
        closestDistance : float = float('inf')
        tolerance = 1e-9

        print("Spot moving towards: " + approachSpot.getSpotAsString())

        for move in moves:
            distance = approachSpot.distanceTo(move.getDestination())
            print("Move option: " + str(move.getMoveAsString()) + " Distance: " + str(distance))
            if (abs(distance - closestDistance) < tolerance):
                movesClosestToApproachSpot.append(move)
            elif (distance < closestDistance):
                movesClosestToApproachSpot.clear()
                closestDistance = distance
                movesClosestToApproachSpot.append(move)
            else:
                print("Move not closer than current high score move")

        
        return movesClosestToApproachSpot[randint(0, len(movesClosestToApproachSpot) - 1)]

