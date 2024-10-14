from pynput import keyboard
import os

# Clear the screen
os.system("clear")


def on_press(key):
	try:
		# Check for q
		if key.char == 'q':
			print('Exiting Program...')
			return False # Stop listener
	except AttributeError:
		pass

	# Check for arrow Keys
	if key == keyboard.Key.up:
		print("Up!")
	elif key == keyboard.Key.down:
		print("Down...")
	elif key == keyboard.Key.left:
		print("<-- Left")
	elif key == keyboard.Key.right:
		print("Right -->")



# Prompt the user
print("Press arrows keys! Press 'q' to exit...")

# Create and start a keyboard listener
with keyboard.Listener(on_press=on_press) as listener: # Create listener object that listens for keyboard events
	listener.join() # Start the listener and wait for it to finish