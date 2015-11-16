# BattleShip game
# V1.0
# Single player - one ship

from random import randint

# create board
board = []
for i in range(0, 5):
    circles = ['O'] * 5
    board.append(circles)

# print board
def print_board(board):
    for row in board:
        print (" ".join(row)) # get rid of quote marks

#pick a row for the boat to be hidden
def random_row(board):
    return randint(0, len(board)-1)

#pick a column for the boat to be hidden
def random_col(board):
    return randint(0, len(board) -1)

#get the boats coordinates from computer
ship_row[] = random_row(board)
ship_col = random_col(board)
print_board(board)
# get the guess from the user
print("Let's play BattleShips!")

for turn in range(0, 5):
    print ("Turn", turn +1)
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Column: ")) - 1

# check for a hit

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sank my battleship")
        break
        board[guess_row][guess_col] = "X"
        print_board(board)
    elif board[guess_row][guess_col] == "X":
        print ("You already guessed that one!")
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print ("Oops, you managed to even miss the ocean!")
        else:
            print ("Sorry! You missed!")
            board[guess_row][guess_col] = "X"
            print_board(board)
if turn == 4:
    print ("Game over")