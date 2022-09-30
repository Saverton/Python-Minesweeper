# tile on a minesweeper board, has flags for is_mine, is_empty, is_flagged, and is_revealed
class Tile:
    def __init__(self, is_mine, is_empty, is_revealed, row, col, board):
        self.is_mine = is_mine,
        self.is_empty = is_empty,
        self.is_revealed = is_revealed,
        self.is_flagged = False
        self.row = row
        self.col = col
        self.board = board
        self.surrounding_mines = 0

    def is_a_mine(self):
        return self.is_mine

    def flag(self):
        self.is_flagged = True

    def reveal(self):
        self.is_revealed = True
        if self.is_mine:
            print("Lose")
        else:
            self.reveal_surrounding()

    def reveal_surrounding(self):
        check_row = max(self.row - 1, 0)
        check_col = max(self.col - 1, 0)
        for row in range(check_row, min(check_row + 3, len(self.board))):
            for col in range(check_col, min(check_col + 3, len(self.board[0]))):
                if self.board[row][col].surrounding_mines == 0:
                    self.board[row][col].reveal()

    def count_surrounding_mines(self):
        check_row = max(self.row - 1, 0)
        check_col = max(self.col - 1, 0)
        count = 0 # count of the number of surrounding mines
        for row in range(check_row, min(check_row + 3, len(self.board))):
            for col in range(check_col, min(check_col + 3, len(self.board[0]))):
                if self.board[row][col].is_a_mine():
                    count += 1
        return count
