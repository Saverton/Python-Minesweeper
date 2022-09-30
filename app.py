from Board import Board

# Goal: to create a basic command prompt based version of minesweeper using Python.
def run_game():
    game_board = Board(10, 10)
    game_over = False

    while not game_over:
        game_board.print_board()
        move = input("Enter action: <row>-<col>-<action>\n\"r\" = reveal, \"f\" = flag\n")
        try:
            col = int(move[0:move.index("-")])
            move = move[move.index("-") + 1:]
            row = int(move[0:move.index("-")])
            move = move[move.index("-") + 1:]
            action = move
            game_board.process_tile(row, col, action)
        except(TypeError):
            print("Invalid input")
        except(GameOver)

run_game()