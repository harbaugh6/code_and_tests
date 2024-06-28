from random import randint

board = []

for i in range(5):
  board.append(["O"] * 5)

def print_board(board_in):
  for i in board:
    print i

# returns a random integer based on the length of the board - 1
def random_row(board_in):
  row = randint(0, len(board_in) - 1)
  return row

# returns a random integer based on the length of the board - 1
def random_col(board_in):
  column = randint(0, len(board_in) - 1)
  return column

# Places a ship in a random location
random_row(board)
random_col(board)

# user input for their guess
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Evaluates the user's row and column guesses.  If they are exact, the user wins.  Otherwise the board is updated with an X for a miss.
for turn in range(4):
  print("Turn"), (turn + 1)
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sunk my battleship!")
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print("Oops, that's not even in the ocean.")
    elif(board[guess_row][guess_col] == "X"):
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
    if turn == 3:
      print ("Game Over")
    board[guess_row][guess_col] = "X"
    print_board(board)