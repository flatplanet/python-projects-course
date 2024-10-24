import random
import os


# Function to generate a math problem
def generate_flashcard(operation):
    # generate two random number
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Logic to do the thing
    if operation == "addition":
        correct_answer = num1 + num2
        question = f'{num1} + {num2} = ?'

    elif operation == "subtraction":
        correct_answer = num1 - num2
        question = f'{num1} - {num2} = ?'

    elif operation == "multiplication":
        correct_answer = num1 * num2
        question = f'{num1} * {num2} = ?'

    elif operation == "division":
        # Ensure the second number is not zero and num1 is divisible by num2
        while num2 == 0 or num1 % num2 != 0:
            # Get new numbers
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        
        correct_answer = num1 // num2
        question = f'{num1} / {num2} = ?'

    # Return the results
    return question, correct_answer


# Main Menu function
def main_menu():
    # Clear the screen
    os.system("clear")
    # Create a menu
    print("\n--- Math Flashcard App ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    # Get the user choice
    choice = input("Choose an option (1-5): ")
    return choice



# Function to create a flashcard session
def flashcard_session(operation):
    while True:
        # clear the screen
        os.system("clear")
        question, correct_answer = generate_flashcard(operation)

        # Print the question
        print(f"\nFlashcard: {question}")

        # Prompt user for answer
        user_answer = input("Your answer: ")

        # Error handling
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

        # Answer solution
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f'Wrong. The correct answer is {correct_answer}')

        # Ask to play again
        next_step = input("\nWould you like another flashcard (y/n)? ").lower()

        if next_step == 'n':
            break


# Main function
def math_flashcard_app():
    while True:
        # Call menu function
        choice = main_menu()

        # Logic to determine choice
        if choice == "1":
            flashcard_session("addition")
        elif choice == "2":
            flashcard_session("subtraction")
        elif choice == "3":
            flashcard_session("multiplication")
        elif choice == "4":
            flashcard_session("division")
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice, please try again.")






# Run the app
math_flashcard_app()