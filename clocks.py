import time
from datetime import datetime
import os
import threading
from zoneinfo import ZoneInfo
# pip install tzdata

# clear the screen
def clear_screen():
	os.system('clear')

# Wait for user to hit enter
def input_thread(stop_event):
	input()
	stop_event.set()



def main():
	# Set up our time zones
	time_zones = {
	'1': ('Eastern Time', 'America/New_York'),
	'2': ('Central Time', 'America/Chicago'),
	'3': ('Pacific Time', 'America/Los_Angeles')
	}
	# Prompt the user to pick a time zone
	print("Select a time zone:")
	# Loop thru our time_zones dictionary
	for key, (name, _) in time_zones.items():
		print(f'{key}. {name}')

	# Assign their selection to a variable
	choice = input("Enter the number of your choice: ").strip()

	# Error handling for choice selection
	if choice not in time_zones:
		print("Invalid Choice. Defaulting to Eastern Time.")
		tz_name = "America/New_York"
		tz_display_name = "Eastern Time"
	else:
		tz_display_name, tz_name = time_zones[choice]


	# Create an event to signal when to stop the clock
	stop_event = threading.Event()

	# Start the input thread
	thread = threading.Thread(target=input_thread, args=(stop_event, ))
	thread.daemon = True
	thread.start()


	# Loop to update our time in seconds till enter is pressed
	while not stop_event.is_set():
		# Clear the screen
		clear_screen()
		# get current time
		#current_time = time.strftime("%H:%M:%S")
		current_time = datetime.now(ZoneInfo(tz_name)).strftime("%I:%M:%S %p")
		# print the current time
		print(f'Current time: {current_time}  - {tz_display_name}')
		# Prompt the user to stop the clock
		print("Press Enter to stop the clock...")
		# run the loop once per second
		time.sleep(1)

	# Print and end message
	print("Clock Stopped...")










# Clear the screen
clear_screen()

# Call the main function
main()