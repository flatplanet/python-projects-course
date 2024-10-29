import os

# Clear
os.system("clear")


# Function to create and save a file
def create_file():
    # Prompt for file details
    text = input("Enter the text you want to save in the file: ")
    file_name = input("Enter the filename (example: myfile.txt): ")
    file_location = input("Enter the file location (c:/python-projects/): ")

    # Ensure the directory exists or create it
    if not os.path.exists(file_location):
        os.makedirs(file_location)

    # Full file path - c:/python-projects/myfile.txt
    file_path = os.path.join(file_location, file_name)

    # Write the text to the file
    with open(file_path, 'w') as file:
        file.write(text)
    print(f"File '{file_name}' saved successfully at {file_location}.")


# Function to open and read a file
def open_file():
    # prompt the user for file details
    file_name = input("Enter the filename to open (example: myfile.txt): ")
    file_location = input("Enter the file location (example: c:/python-projects/): ")

    # Get the full path
    file_path = os.path.join(file_location, file_name)

    # Check if the file exists
    if os.path.exists(file_path):
        # Read and output the file contensts
        with open(file_path, 'r') as file:
            # Print the contents
            print("\nFile Contents:")
            print(file.read())
    else:
        print(f"File '{file_name}' not found at {file_location}.")




# The main function
def file_manager():
    while True:
        print("\n--- File Manager ---")
        print("1. Create and save a file")
        print("2. Open and read a file")
        print("3. Quit")

        # Get selection
        choice = input("Choose and option (1/2/3): ")

        if choice == "1":
            create_file()
        elif choice == "2":
            open_file()
        elif choice == "3":
            print("Exiting the program. Later duder!")
            break
        else:
            print("Invalid selection. Please choose 1, 2, or 3.")







# Call the program
file_manager()