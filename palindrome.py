import os

os.system("clear")

def is_palindrome(string):
	# Remove the spaces and covert to lowercase and strip notation
	'''
	cleaned_string = ''
	# Loop through our user input
	for character in string:
		# Check to see if the charcer is a charcter
		if character.isalnum():
			cleaned_string += character.lower()
	'''
	# Shorthand for the above code:
	cleaned_string = ''.join(character.lower() for character in string if character.isalnum())


	# Check if the string is the same forwards and backwards
	return cleaned_string == cleaned_string[::-1] # backwards slicey thing





# Ask the user for input
user_input = input("Enter a Word or phrase to check if it's a palindrome: ")

# Slice = [start:stop:step]
#user_input = user_input[::-1]

# Check if true or false
if is_palindrome(user_input):
	print(f'{user_input} is a palindrome!')
else:
	print(f'{user_input} is NOT a palindrome!')



