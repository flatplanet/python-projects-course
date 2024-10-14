import random
import string
import os

# Clear the screen
os.system("clear")
print(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
# Actually validate the password:
def validate_password(password):
	# Check our password rules
	if len(password) < 8:
		return False, "Password must be at least 8 character long."
	# Check for digits
	if not any(char.isdigit() for char in password):
		return False, "Password must contain at least one digit."
	# Check for lowercase
	if not any(char.islower() for char in password):
		return False, "Password must contain at least one lowercase letter."
	# Check for uppercase
	if not any(char.isupper() for char in password):
		return False, "Password must contain at least one r."
	# Check for special characters
	if not any(char in string.punctuation for char in password):
		return False, "Password must contain at least one special character."
	
	# Return true if all the rules were true
	return True, "Password is strong!!"

# Generate the password
def generate_password(length):
	while True:
		# Ensure we meet the basic criteria (the four things) at least once 
		password = [
			random.choice(string.ascii_lowercase), # At least one lowercase
			random.choice(string.ascii_uppercase), # At least one uppercase
			random.choice(string.digits), # At least one digit
			random.choice(string.punctuation), # At least one special character
		]

		# Fill the rest of the password with random characters from all the charcter sets
		# Get remaining character count
		remaining_length = length - 4
		# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
		password += random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=remaining_length)
		# password = ["s", "G", "6", "%", "9", "$", "H", "1"]
		
		# Shuffle the list
		random.shuffle(password)

		# Convert our list into a string using join()
		password = ''.join(password)

		# Validate 
		is_valid, message = validate_password(password)
		if is_valid:
			return password


# Prompt the user
def password_generator():
	while True:
		try:
			# get the password length
			length = int(input("Enter the desired password length (minimum 8): "))
			if length < 8:
				print("Password length mush be at least 8 characters.")
				continue
			break
		except ValueError:
			print("Invalid input. Please enter a number.")

	# Generate the password
	password = generate_password(length)
	print(f'Generated Password: {password}')
	print("This password is strong!")




# Run the progam
#password_generator()