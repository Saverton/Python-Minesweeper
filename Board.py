from Tile import Tile
import random

# board class for minesweeper
class Board:

    def __init__(self, width, height):
        self.board_tiles = []
        for row_index in range(height):
            self.board_tiles.append([])
            for col_index in range(width):
                self.board_tiles[row_index].append(Tile(row_index, col_index, self.board_tiles))
        self.generate_board(10) # generate the board with 10 mines

    # generate a random minesweeper board with x max number of mines
    def generate_board(self, number_of_mines):
        for index in range(number_of_mines):
            random_row = random.randint(0, len(self.board_tiles) - 1)
            random_col = random.randint(0, len(self.board_tiles[0]) - 1)
            self.board_tiles[random_row][random_col].is_mine = True
        for row in self.board_tiles:
            for tile in row:
                if not tile.is_mine:
                    tile.count_surrounding_mines()
        random_row = random.randint(0, len(self.board_tiles) - 1)
        random_col = random.randint(0, len(self.board_tiles[0]) - 1)
        while self.board_tiles[random_row][random_col].is_mine or self.board_tiles[random_row][random_col].surrounding_mines > 0:
            random_row = random.randint(0, len(self.board_tiles) - 1)
            random_col = random.randint(0, len(self.board_tiles[0]) - 1)
        self.board_tiles[random_row][random_col].reveal() # reveal starting tile

    def process_tile(self, row, col, action):
        try:
            if action == "f":
                print("Flagging (" + str(row) + ", " + str(col) + ")")
                self.board_tiles[col][row].flag()
            elif action == "r":
                print("Revealing (" + str(row) + ", " + str(col) + ")")
                self.board_tiles[col][row].reveal()
            else:
                raise TypeError("Invalid action")
        except(IndexError):
            print("Invalid coordinate")
        except(Exception):
            print(Exception)
        
    # print the minesweeper board
    def print_board(self):
        width = len(self.board_tiles[0]) # number of columns in the board
        Board.print_board_top_header(width) # print the top row (which is a header)
        Board.print_board_horizontal_line(width) # print a line to cover the screen
        for row_index in range(len(self.board_tiles)): # loop through and print each row
            Board.print_board_row(self.board_tiles[row_index], row_index)
            Board.print_board_horizontal_line(width)
        print() # line break at the end
        pass

    # print the top header row in the minesweeper board
    def print_board_top_header(board_width):
        line = "   |" # leave space above left side header
        for index in range(board_width):
            line += " " + str(index) + " |"
        print(line)

    # print a line that covers the width of a board given the width of the board
    def print_board_horizontal_line(board_width):
        line = "----"
        for index in range(board_width):
            line += "----"
        print(line)

    # print a row in a minesweeper board
    def print_board_row(board_row, index):
        line = " " + str(index) + " |"
        for tile in board_row:
            line += " " + tile.get_tile_string() + " |"
        print(line)