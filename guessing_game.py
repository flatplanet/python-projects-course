# Import the os module/library
import os
# Import the random library
import random

# Create a play again function
def play_again():
	# Prompt the user
	again = input("Would you like to play again? y/n ")
	# Logic to figure out what to do
	if again == "y" or again == "yes" or again == "YES" or again == "Yes":
		game()
	else:
		print("Thanks for playing!")
		return

# Create our main game function
def game():
	# Create a variable to keep track of the number of guesses
	number_of_guesses = 0
	correct = False

	# Clear The Screen
	os.system("clear")

	# Generate a random number and assign it to a variable
	number_to_guess = random.randint(1,10)

	# Get user input
	print("Guess a Number between 1 and 10")

	# Create guessing loop
	while correct == False:
		# Try/except block
		try:
			guess = int(input("Enter your Guess: "))
		except Exception as e:
			print("Something went wrong! Game Over")
			return

		# Create some logic to check the guess
		if guess < number_to_guess:
			print("Too Low! - Try Again!")
			# Increment the number of guesses
			number_of_guesses += 1
		elif guess > number_to_guess:
			print("Too High! - Try Again!")
			# Increment the number of guesses
			number_of_guesses += 1

		elif guess == number_to_guess:
			# Increment the number of guesses
			number_of_guesses += 1
			print(f"Correct! The number was {number_to_guess} and you guessed it in {number_of_guesses} guesses!")
			# Set correct to TRUE
			correct = True
			# Run the play_again Function to see if the user wants to play again
			play_again()




# Call our game function
game()