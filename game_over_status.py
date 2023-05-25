from enum import Enum

class GameOverStatus(Enum):
    IN_PROGRESS = 0
    WHITE_WIN = 1
    BLACK_WIN = 2
    DRAW = 3