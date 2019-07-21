#Sam Lyons
#CIS-294
#3/23/19
#Assignment 7

"""A program that emulates and runs
	a game of battleship."""

from random import randint
board = []

for x in range (0, 5):
	board.append(["0"] * 5)

def print_board(board):
	for row in board:
		print(" ".join(row))

print_board(board)		

def random_row(board):
	return randint(0, len(board) - 1)
	
def random_col(board):	
	return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#uncomment following statements to allow player to view ship location on board.

#print ship_row
#print ship_col

for turn in range(4): #for loop with main functions of battleship game.
	print("Turn: ", turn + 1)
	guess_row = int(input("Guess Row: "))
	guess_col = int(input("Guess Col: "))

	if guess_row == ship_row and guess_col == ship_col: #correct input for battleship
		print("Congratulations! You sank my battleship!")
		break
	else:
		if guess_row not in range(5) or guess_col not in range(5): # statements if miss or invalid input.
			print("Oops! that's not even in the ocean. ")
		elif board[guess_row][guess_col] == "X":
			print("You guessed that one already. ")
		else:
			print("You missed my battleship! ")
			board[guess_row][guess_col] = "X"
		if (turn == 3):
			print("Game Over")
		print_board(board)				












