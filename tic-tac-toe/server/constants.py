from enum import Enum


class TicTacToeDirections(Enum):
    """ Holds tuples of integers, representing the X and Y values we should add/subtract to go in the given direction
        of a 2D Matrix """
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    UPRIGHT = (-1, 1)
    UPLEFT = (-1, -1)
    DOWNRIGHT = (1, 1)
    DOWNLEFT = (1, -1)
    DOWN = (1, 0)


class TicTacToeRows(Enum):
    """
    Holds tuples of two TicTacToeDirections, effectivelly representing a valid row
    i.e LEFT and RIGHT would be the horizontal row
        UPRIGHT and DOWNLEFT would be one diagonal
    """
    HORIZONTAL_ROW = (TicTacToeDirections.LEFT, TicTacToeDirections.RIGHT)
    VERTICAL_ROW = (TicTacToeDirections.UP, TicTacToeDirections.DOWN)
    LEFT_DIAGONAL_ROW = (TicTacToeDirections.UPLEFT, TicTacToeDirections.DOWNRIGHT)
    RIGHT_DIAGONAL_ROW = (TicTacToeDirections.UPRIGHT, TicTacToeDirections.DOWNLEFT)

TIC_TAC_TOE_SYMBOLS = ['O', 'X', 'A', 'R', "V", "S", "E", "Q"]
MAX_TIC_TAC_TOE_PLAYERS = 10