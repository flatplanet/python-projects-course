import os
import random

# clear screen
os.system("clear")

# creating a list of words 
word_list = ['python', 'javascript', 'ruby', 'perl', 'hangman', 'developer', 'coder', 'variable', 'syntax', 'function']

# Select random word from our word_list
def get_random_word():
	return random.choice(word_list)

# Display the current state of the guessed word
def display_word(word, guessed_letters):
	return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Main game logic
def play_hangman():
	# Get the random word
	word = get_random_word()
	# Get the length of that word
	word_length = len(word)

	# Keep track of guessed letters and incorrect gueses
	# my_set = {"python", "ruby", "js"}
	# sets can't have duplicates, so same letter cant be guessed multiple times
	# can check them faster than scanning a list
	guessed_letters = set() # letters the player guessed correctly
	incorrect_guesses = set() # incorrect letters guessed by the player
	lives = 6 # number of incorrect guesses allowed

	# Prompt the user
	print("Welcome to Hangman!")
	print(f'The word has {word_length} letters')

	# Main game loop
	while lives > 0:
		# Display the current word status
		print("\n" + display_word(word, guessed_letters))
		print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
		print(f'Lives Remaining: {lives}')

		# Prompt the user for a guess
		guess = input("Guess a letter: ").lower()

		# Validate the guesses
		if len(guess) != 1 or not guess.isalpha():
			os.system("clear")
			print("Invalid input. Please enter a single letter.")
			continue
		# Check if the letter has already been guessed
		if guess in guessed_letters or guess in incorrect_guesses:
			os.system("clear")
			print(f"You already guessed {guess}. Try a different letter.")
			continue
		# Check if the guess is correct
		if guess in word:
			os.system("clear")
			guessed_letters.add(guess)
			print(f'Good Guess! "{guess}" is in the word.')
		else:
			os.system("clear")
			incorrect_guesses.add(guess)
			# remove a life
			lives -= 1
			print(f'Wrong Guess! "{guess}" is not in the word.')

		# check if the player has guessed the entire word
		if all(letter in guessed_letters for letter in word):
			print(f"\nCongrats!! You guessed the word: {word}")
			break



	# if the player runs out of lives
	if lives == 0:
		print("\nYou ran out of lives! The word was: ", word)




play_hangman()