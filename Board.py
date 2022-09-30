# board class for minesweeper
class Board:

    def __init__(self, width, height):
        self.board_tiles = []
        for row_index in range(height):
            self.board_tiles.append([])
            for col_index in range(width):
                self.board_tiles[row_index].append("a")
        
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
        for index in board_row:
            line += " " + str(index) + " |"
        print(line)