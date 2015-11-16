# BattleShip game
# V1.0
# Single player - multiple ships

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
boats = 2
ship_row_1 = random_row(board)
ship_col_1 = random_col(board)
ship_row_2 = random_row(board)
ship_col_2 = random_col(board)
if ship_row_2 == ship_row_1 and ship_col_2 == ship_col_1:
    if ship_row_2 > 1:
        ship_row_2 = ship_row_2- 1
    elif ship_row_2 < 1:
        ship_row_2 = ship_row_2 + 1
print_board(board)

# get the guess from the user
print("Let's play BattleShips!")
print("There are", boats, "Battleships!")
turn = 0
while turn < 5:
    turn += 1
    print ("Turn", turn)
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Column: ")) - 1

# check for a hit

    if guess_row == ship_row_1 and guess_col == ship_col_1 or guess_row == ship_row_2 and guess_col == ship_col_2:
        turn -= 1
        board[guess_row][guess_col] = "B"
        if board[ship_row_1][ship_col_2] and board[ship_row_2][ship_col_2] != "B":
            print ("Congratulations! You sank my first battleship")
            print ("Have an extra turn!")
        else:
            print ("Congratulations! You sank all of my Battleships!\nYou win!")

        if board[ship_row_1][ship_col_2] and board[ship_row_2][ship_col_2] == "B":
            break
        else:
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
if turn == 4 and board[ship_row_1][ship_col_2] and board[ship_row_2][ship_col_2] != "B":
    print ("Game over")
