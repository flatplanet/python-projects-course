# Import Tkinter
from tkinter import *
# Import the os module/library
import os
# Import the random library
import random




# Create a play again function
def reset_game(guess_entry, result_label, submit_button, play_again_button, state):
	# Generate a random number and assign it to a variable
	state['number_to_guess'] = random.randint(1,10)
	# Set number of guesses to zero
	state['number_of_guesses'] = 0
	# Delete result label
	result_label.config(text="")
	# Clear the entry box
	guess_entry.delete(0, END)
	# Set the submit button back to normal
	submit_button.config(state=NORMAL)
	# Hide the play again button...again
	play_again_button.pack_forget()



# Create our main game function
def check_guess(guess_entry, result_label, submit_button, play_again_button, state):

	# Try/except block
	try:
		guess = int(guess_entry.get())
		state['number_of_guesses'] +=1
		# Create some logic to check the guess
		if guess < state['number_to_guess']:
			result_label.config(text="Too Low! - Try Again!")

		elif guess > state['number_to_guess']:
			result_label.config(text="Too High! - Try Again!")

		else:
			result_label.config(text=f"Correct! The number was {state['number_to_guess']} and you guessed it in {state['number_of_guesses']} guesses!")
			# Disable the guess button
			submit_button.config(state=DISABLED)
			# Enable the play again button
			play_again_button.pack()

	except ValueError:
		result_label.config(text="Invalid Input! Please enter a number.")

	



def setup_gui():
	# Create the window
	root = Tk()
	# Add a title
	root.title("Guessing Game")
	# Set the size of the app
	root.geometry('500x350')

	# Set the game state
	state = {'number_to_guess':None, 'number_of_guesses':0}

	# Create a Label
	instruction_label = Label(root, text="Guess a Number between 1 and 10", font=("Helvetica", 18))
	instruction_label.pack(pady=20)

	# Create an entry box
	guess_entry = Entry(root, font=("Helvetica", 18))
	guess_entry.pack(pady=10)

	# Create another Label
	result_label = Label(root, text="")
	result_label.pack(pady=20)


	# Create some buttons
	submit_button = Button(root, text="Submit Guess", command=lambda: check_guess(guess_entry, result_label, submit_button, play_again_button, state))
	submit_button.pack(pady=20)

	play_again_button = Button(root, text="Play Again?", command=lambda: reset_game(guess_entry, result_label, submit_button, play_again_button, state))
	play_again_button.pack()
	# Hide this button
	play_again_button.pack_forget()





	# On start, reset the game
	reset_game(guess_entry, result_label, submit_button, play_again_button, state)

	# Start the app
	root.mainloop()


# Call our main function'
setup_gui()