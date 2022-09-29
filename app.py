# Goal: to create a basic command prompt based version of minesweeper using Python.

# print the minesweeper board
def print_board(board_array):
    width = len(board_array[0]) # number of columns in the board
    print_board_top_header(width) # print the top row (which is a header)
    print_board_horizontal_line(width) # print a line to cover the screen
    for row_index in range(len(board_array)): # loop through and print each row
        print_board_row(board_array[row_index], row_index)
        print_board_horizontal_line(width)
    print()# line break at the end
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

example_board = [ 
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
]
print_board(example_board)