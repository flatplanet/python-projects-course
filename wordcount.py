import os

# Clear the screen
os.system("clear")


# Function to count the number of words in a sentence
def count_words(sentence):
	# split our sentence into a python list
	words = sentence.split()
	
	# john elder is cool
	# words = ["john", "elder", "is", "cool"]

	# Get the length of the list with len()
	return len(words)

# Function to count the number of characters including spaces
def count_characters_with_spaces(sentence):
	# use the len
	return len(sentence)


# Function to count the number of characters excluding spaces
def count_characters_without_spaces(sentence):
	# Remove the spaces from our sentence
	return len(sentence.replace(" ", "")) # .replace('thing to replace', 'thing to replace it with')




# Main function
def word_count_program():
	# Prompt the user
	sentence = input("Enter a sentence: ")

	if sentence:
		# Get word count and character counts
		word_count = count_words(sentence)
		char_count_with_spaces = count_characters_with_spaces(sentence)
		char_count_without_spaces = count_characters_without_spaces(sentence)

	else:
		print("That's not a sentence")

	# Print the results
	print(f'Word Count: {word_count}')
	print(f'Character Count (with spaces): {char_count_with_spaces} ')
	print(f'Character Count (without spaces): {char_count_without_spaces} ')

# Run the program
word_count_program()


