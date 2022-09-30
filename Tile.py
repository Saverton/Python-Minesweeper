# tile on a minesweeper board, has flags for is_mine,  is_flagged, and is_revealed
from GameOverException import GameOverException


class Tile:
    def __init__(self, row, col, board):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.row = row
        self.col = col
        self.board = board
        self.surrounding_mines = 0

    # flag a tile
    def flag(self):
        self.is_revealed = True
        self.is_flagged = True

    # reveal a tile
    def reveal(self):
        self.is_revealed = True
        self.is_flagged = False
        if self.is_mine:
            raise GameOverException("You Lose!")
        elif self.surrounding_mines == 0:
            self.reveal_surrounding()

    # reveal any surrounding tiles recursively that have no surrounding mines
    def reveal_surrounding(self):
        check_row = max(self.row - 1, 0)
        check_col = max(self.col - 1, 0)
        for row in range(check_row, min(self.row + 2, len(self.board))):
            for col in range(check_col, min(self.col + 2, len(self.board[0]))):
                if not self.board[row][col].is_revealed:
                    self.board[row][col].reveal()

    # count the surrounding tiles that are mines
    def count_surrounding_mines(self):
        check_row = max(self.row - 1, 0)
        check_col = max(self.col - 1, 0)
        count = 0 # count of the number of surrounding mines
        for row in range(check_row, min(self.row + 2, len(self.board))):
            for col in range(check_col, min(self.col + 2, len(self.board[0]))):
                if self.board[row][col].is_mine:
                    count += 1
        self.surrounding_mines = count

    # get the string that is used to display this tile on the board
    def get_tile_string(self):
        if self.is_revealed:
            if self.is_flagged:
                return "F"
            elif self.is_mine:
                return "M"
            else:
                return str(self.surrounding_mines)
        else:
            return " "