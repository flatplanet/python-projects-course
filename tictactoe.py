import os

# Clear the screen
def clear_screen():
	os.system("clear")


'''
1 | 2 | 3
--+---+--
4 | O | 6
--+---+--
7 | 8 | 9

'''

# Print the board
def print_board(board):
	print(f"{board[0]} | {board[1]} | {board[2]}")
	print("--+---+--")
	print(f"{board[3]} | {board[4]} | {board[5]}")
	print("--+---+--")
	print(f"{board[6]} | {board[7]} | {board[8]}")
	print()

# Check for winner
def check_winner(board, current_player):
	# Define winning combinations are
	win_combinations = [
		[0,1,2], [3,4,5], [6,7,8], # rows
		[0,3,6], [1,4,7], [2,5,8], # columns
		[0,4,8], [2,4,6], 		   # diagonals
	]

	# Check if any winning combination is met
	for combination in win_combinations:
		if board[combination[0]] == board[combination[1]] == board[combination[2]] == current_player:
			return True
	return False



# Check if draw
def check_draw(board):
	# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	return all(spot in ["X", "O"] for spot in board)






# Main function
def play_tic_tac_toe():
	# Initialze the board (empty spots represented by numbers)
	# ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	board = [str(i) for i in range(1,10) ]

	# Define our players
	current_player = "X"

	# Main game loop
	while True:
		clear_screen()
		print_board(board)

		# Get player move
		move = input(f"Player {current_player}, enter your move (1-9)")

		# Validate the move 
		if not move.isdigit() or int(move) < 1 or int(move) > 9:
			print("Invalid Input. Please enter a number between 1 and 9.")
			continue

		# Convert move number to index number by subtracting 1
		move = int(move) - 1

		# Check if the spot is already taken
		if board[move] in ["X", "O"]:
			print("That spot is already taken. Try again")
			continue

		# Update the board
		# ['X', '2', '3', '4', '5', '6', '7', '8', '9']
		board[move] = current_player

		# Check if the current player has won
		if check_winner(board, current_player):
			clear_screen()
			# Redraw the updated board
			print_board(board)
			print(f'Player {current_player} wins!')
			break

		# Check if game is draw
		if check_draw(board):
			clear_screen()
			print_board(board)
			print("It's a Draw!")
			break



		# Switch players
		current_player = 'O' if current_player == "X" else "X"



# Play the game
play_tic_tac_toe()