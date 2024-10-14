import string
import os


# Clear the screen
os.system("clear")


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
		return False, "Password must contain at least one uppercase letter."
	# Check for special characters
	if not any(char in string.punctuation for char in password):
		return False, "Password must contain at least one special character."
	
	# Return true if all the rules were true
	return True, "Password is strong!!"


# Print out the password rules
def show_password_rules():
	print("Password Rules:")
	print("1. Must be at least 8 characters long.")
	print("2. Must contain at least one digit (0-9).")
	print("3. Must contain at least one lowercase letter (a-z).")
	print("4. Must contain at least one uppercase letter (A-Z).")
	print("5. Must contain at least one special character (!, @, #, $, etc.).")
	print()


def password_validator():
	# Show the password rules
	show_password_rules()

	# Prompt the user for their password
	password = input("Please enter your password: ")

	# Validate the password
	bob, message = validate_password(password)

	# Return the result
	if bob:
		print("Success: ", message)
	else:
		print("Validation Failed: ", message)


# run the program
password_validator()