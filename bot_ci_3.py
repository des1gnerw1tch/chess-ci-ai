from argparse import ArgumentError
from i_player import IPlayer
from i_move import IMove
from i_chess_model_state import IChessModelState
from i_spot import ISpot
from piece import Piece, pieceToValueNorm
from bot_utils import getRandomSpotToMoveFrom, getHighestCaptureMove, getMovesFromSpot
from player_color import PlayerColor
from typing import List
from random import randint, random, uniform
from math import sqrt

class GenomeBotCI3:
    """
    The genome for BotCI3. Contains all the behavioral characteristics of the bot. 
    """
    def __init__(self, proximityWeight: float, pieceValueWeight: float,
                maxProximityDistance: float, chanceGoForKing: float):
        self.proximityWeight = proximityWeight
        self.pieceValueWeight = pieceValueWeight
        self.maxProximityDistance = maxProximityDistance

        if (chanceGoForKing > 1 or chanceGoForKing < 0):
            raise ArgumentError("Chance go for king has to be between 0-1")
        
        self.chanceGoForKing = chanceGoForKing

    def crossover(self, other_parent : 'GenomeBotCI3') -> 'GenomeBotCI3':
        proximityWeight = None
        pieceValueWeight = None
        maxProximityDistance = None
        chanceGoForKing = None

        num1, num2, num3= randint(0,1), randint(0,1), randint(0,1)
        if num1 == 0:
            proximityWeight = self.proximityWeight
            pieceValueWeight = self.pieceValueWeight
        else:
            proximityWeight = other_parent.proximityWeight
            pieceValueWeight = other_parent.pieceValueWeight
            
        if num2 == 0:
            maxProximityDistance = self.maxProximityDistance
        else:
            maxProximityDistance = other_parent.maxProximityDistance

        if num3 == 0:
            chanceGoForKing = self.chanceGoForKing
        else:
            chanceGoForKing = other_parent.chanceGoForKing

        return GenomeBotCI3(proximityWeight, pieceValueWeight, maxProximityDistance, chanceGoForKing)

    """
    Mutates a genome by a mutation scale. mutation_scale defines the maximum relative difference between 
    original value and mutated value.
    """
    def mutate(self, mutation_scale : float = 0.1) -> 'GenomeBotCI3':
        proximityWeight = self.proximityWeight
        pieceValueWeight = self.pieceValueWeight
        maxProximityDistance = self.maxProximityDistance
        chanceGoForKing = self.chanceGoForKing

        num = randint(0, 3)
        mutation_num = uniform(1 - mutation_scale, 1 + mutation_scale)

        if num == 0:
            proximityWeight *= mutation_num
        elif num == 1:
            pieceValueWeight *= mutation_num
        elif num == 2:
            maxProximityDistance *= mutation_num
        elif num == 3:
            chanceGoForKing = self._clamp(chanceGoForKing * mutation_num, 0, 1)
        
        return GenomeBotCI3(proximityWeight, pieceValueWeight, maxProximityDistance, chanceGoForKing)

    def _clamp(self, v, min_val, max_val):
        return max(min(v, max_val), min_val)

    @staticmethod
    def create_random() -> 'GenomeBotCI3':
        #uniform(0, sqrt(128)) TODO: Fix the variable seeing distance
        return GenomeBotCI3(randint(0, 10), randint(0, 10), 10000, random())

    def to_string(self) -> str:
        return "Proximity Weight: " + str(self.proximityWeight) + " Piece Value Weight " + str(self.pieceValueWeight) + " Max Proximity Distance " + str(self.maxProximityDistance) + " Chance go for King " + str(self.chanceGoForKing)



class BotCI3(IPlayer):
    """
    An AI player where will choose a random piece to move, and that piece will try to capture 
    the maximum value piece. If that piece can't find a capture, it will move closer to a 
    piece depending on weights of a couple factors.

    Builds on BotCI2 by allowing pieces to go for the king more often. The pieces will go for the 
    king based on a given chance (chanceForKing) when there are no capturing moves. 
    """

    @staticmethod
    def create_from_genome(state: IChessModelState, genome : GenomeBotCI3, show_debug : bool = True) -> IPlayer:
        return BotCI3(state, genome.proximityWeight, genome.pieceValueWeight, genome.maxProximityDistance, genome.chanceGoForKing, show_debug)

    
    def __init__(self, state : IChessModelState, proximityWeight: float, pieceValueWeight: float,
                maxProximityDistance: float, chanceGoForKing: float, show_debug = True) -> None:
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
        self.show_debug = show_debug

        if (chanceGoForKing > 1 or chanceGoForKing < 0):
            raise ArgumentError("Chance go for king has to be between 0-1")
        
        self.chanceGoForKing = chanceGoForKing


    def getNextMove(self) -> IMove:
        spot = getRandomSpotToMoveFrom(self.state)
        maxCaptureMove = getHighestCaptureMove(self.state, spot)
        if maxCaptureMove is None:
            spotToApproach = self._getSpotToApproach(spot)
            move = self._approachSpot(spot, spotToApproach)
            if (self.show_debug):
                print("Non capture move selected")
            result = move
        else:
            result = maxCaptureMove
        
        if (self.show_debug):
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

        if (self.show_debug):
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
            if (self.show_debug):
                print("No pieces left to follow! Now will check if king is visible")
            if (kingSpot is None):
                if (self.show_debug):
                    print("No kings are visible. Will choose a random spot to move to.")
                randMoves = getMovesFromSpot(self.state, attackingSpot)
                return randMoves[randint(0, len(randMoves) - 1)].getDestination()
            else:
                if (self.show_debug):
                    print("Moving towards king!")
                return kingSpot
            
        # Decide if want to go for king or to go for highest scoring enemy spot, dependent on probablility
        r = random()
        if (self.show_debug):
            print("Chance go for king: " + str(self.chanceGoForKing) + " float chosen: " + str(r))
        if (r < self.chanceGoForKing):
            if (self.show_debug):
                print("Going for king!")
            return kingSpot
        else:
            if (self.show_debug):
                print("Going for highest scoring enemy spot/s")
            return highestScoringEnemySpots[randint(0, len(highestScoringEnemySpots) - 1)]


    def _calculateSpotScore(self, locationOfAttackingPiece : ISpot, enemySpot : ISpot) -> float:
        proximityScore = locationOfAttackingPiece.distanceToNorm(enemySpot) * self.proximityWeight
        pieceValueScore = pieceToValueNorm(self.state.getPieceAtSpot(enemySpot)) * self.pieceValueWeight

        if (self.show_debug):
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

        if (self.show_debug):
            print("Spot moving towards: " + approachSpot.getSpotAsString())

        for move in moves:
            distance = approachSpot.distanceTo(move.getDestination())
            if (self.show_debug):
                print("Move option: " + str(move.getMoveAsString()) + " Distance: " + str(distance))
            if (abs(distance - closestDistance) < tolerance):
                movesClosestToApproachSpot.append(move)
            elif (distance < closestDistance):
                movesClosestToApproachSpot.clear()
                closestDistance = distance
                movesClosestToApproachSpot.append(move)
            else:
                if (self.show_debug):
                    print("Move not closer than current high score move")

        
        return movesClosestToApproachSpot[randint(0, len(movesClosestToApproachSpot) - 1)]

