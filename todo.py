import os


#clear the screen
os.system("clear")

# Our list will be in this format:
'''
 tasks = [i
 		{"task": "Walk the dog", "completed": False},
		{"task": "Take a nap", "completed": True},
		{"task": "Wash the car", "completed": False}
	]

'''

# Add a task to the list
def add_task(tasks, task):
	# append the new task onto our tasks list
	tasks.append({"task": task, "completed": False})
	print(f'Task "{task}" has been added.')
	return tasks

# View the tasks on the list
def view_tasks(tasks):
	if not tasks:
		print("No Tasks In The List...")
	else:
		print("\nTo-Do List:")
		for idx, task_info in enumerate(tasks, 1):
			status = "Done" if task_info["completed"] else "Not Done"
			print(f'{idx}. {task_info["task"]} - {status}')
	print()






# Remove a task from the list
def remove_task(tasks, task_index):
	if 0 <= task_index < len(tasks):
		removed_task = tasks.pop(task_index)
		#{"task": "Walk the dog", "completed": False},
		print(f'Removed Task: {removed_task['task']}')
	else:
		print("Invalid Task Number.")
	return tasks
	



# Mark a task as complete
def mark_task_completed(tasks, task_index):
	if 0 <= task_index < len(tasks):
		# Update that item
		tasks[task_index]["completed"] = True
		# Print some output
		print(f'Task "{tasks[task_index]["task"]}" marked as completed.')
	else:
		print("Invalid Task Number")

	return tasks


# Main todo function
def to_do_list_app():
	# Create a python list to keep track of our todo list
	tasks = []

	while True:
		# Clear the screen
		os.system("clear")

		print("\n--- To-Do List Menu ---")
		print("1. Add Task")
		print("2. View Tasks")
		print("3. Remove Task")
		print("4. Mark Task as Completed")
		print("5. Quit")

		choice = input("Choose An Option: ")

		# Add Task
		if choice == '1':
			task = input("Enter the Task: ")
			tasks = add_task(tasks, task)
			# tell the user to hit enter
			input("\nPress Enter to Continue...") # pause before clearing the screen

		# View Tasks
		elif choice == '2':
			view_tasks(tasks)
			input("\nPress Enter to Continue...") # pause before clearing the screen

		# Remove tasks
		elif choice == '3':
			# Check to make sure there are tasks
			if tasks:
				view_tasks(tasks) # show the list before prompting the user to remove one
				task_index = int(input("Enter the task number to remove: ")) - 1
				# Call the remove task function and pass in the list and item to remove
				tasks = remove_task(tasks, task_index)
			else:
				print("There are no tasks to remove...")
			input("\nPress Enter to Continue...") # pause before clearing the screen

		# Mark Task as completed
		elif choice == '4':
			# Check to make sure there are tasks
			if tasks:
				# view the list
				view_tasks(tasks) # show the list before prompting the user to remove one
				task_index = int(input("Enter the task number to mark as completed: ")) - 1
				# Call the markt_task_completed function and pass in the list and item to update
				tasks = mark_task_completed(tasks, task_index)
			else:
				print("There are no tasks to mark as completed...")
			input("\nPress Enter to Continue...") # pause before clearing the screen

		# Quit
		elif choice == '5':
			print("Exiting To-Do List. Goodbye!")
			break

		else:
			print("Invalid option. Please Try Again")
			input("\nPress Enter to Continue...") # pause before clearing the screen




# Run the app
to_do_list_app()	
