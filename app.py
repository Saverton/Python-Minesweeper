from Board import Board
from GameOverException import GameOverException

# Goal: to create a basic command prompt based version of minesweeper using Python.
def run_game():
    game_board = Board(10, 10)
    game_over = False

    while not game_over:
        game_board.print_board()
        move = input("Enter action: <row><col><action>\n\"r\" = reveal, \"f\" = flag\n")
        try:
            row = int(move[0])
            col = int(move[1])
            action = move[2]
            game_board.process_tile(row, col, action)
        except (TypeError, ValueError):
            print("Invalid input")
        except GameOverException as e:
            game_board.print_board()
            print(e)
            game_over = True

run_game()