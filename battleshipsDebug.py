from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board) 
ship_col = random_col(board)

# for testing purposes, print actual location
print (ship_row + 1) 
print (ship_col + 1)

print ("\nYou have Six Guess to find the ship\nUse numbers 1 to 5 for the rows and columns\n")
print_board(board)
print('\n')

win_state = False
for i in range (6):
  guess_row = int(input("Guess Row: "))-1
  guess_col = int(input("Guess Col: "))-1
  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!\n")
    board[guess_row][guess_col] = "*"
    print_board(board)
    win_state = True
    break
  elif guess_row not in range(5) and guess_col not in range(5):
    print ("Oops, that's not even in the ocean.")
  elif board[guess_row][guess_col] == "X":
    print ("You guessed that one already.\n you'v lost a turn")
  else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      print_board(board)

if win_state == False:
  print("\nYou didn't hit my battleship and are out of guesses\n")
else:
  print("\nWell done\n")
