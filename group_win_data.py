"""
Wins, draws, losses, and total wins for a named group against an opponent
"""
class GroupMatchData():
    number : int = -1 # e.g. "800", "1"
    number_label : str = None # e.g. "StockfishELO", "Generation"
    opponent : str = None
    wins : int = 0
    draws : int = 0
    losses : int = 0

    def __init__(self, number, number_label, opponent, wins, draws, losses):
        self.number = number
        self.number_label = number_label
        self.opponent = opponent
        self.wins = wins
        self.draws = draws
        self.losses = losses

    def getTotalGames(self):
        return self.wins + self.draws + self.losses
