import subprocess
import os

# Clear the screen
os.system("clear")

# Function to run a selected Python file:
def run_file(filename):
    try:
        # Run the file
        subprocess.run(["winpty", "python", filename], check=True)

    except subprocess.CalledProcessError:
        print(f"Error: Could not run {filename}")


# Main function
def main_menu():
    while True:
        
        print("\n--- Main Menu ---")
        print("1. Anagram Solver")
        print("2. Use Arrows")
        print("3. Use Arrows With Tkinter")
        print("4. Choose Your Own Adventure")
        print("5. Clocks")
        print("6. Draw Turtles")
        print("7. Open Save Filez")
        print("8. Flashcard Game")
        print("9. Password Generator")
        print("10. Number Guessing Game")
        print("11. Number Guessing Game GUI")
        print("12. Hangman Game")
        print("13. Images")
        print("14. Palindrome Checker")
        print("15. Rock Paper Scissors")
        print("16. Typing Speed Texts")
        print("17. Tic Tac Toe")
        print("18. To-Do List")
        print("19. Password Validator")
        print("20. Word Counter")
        print("21. Quit")
        
        # Get choice
        choice = input("Choose an option (1-21): ")

        if choice == '1':
            run_file('anagram.py')
        elif choice == '2':
            run_file('arrows.py')
        elif choice == '3':
            run_file('arrows-tkinter.py')
        elif choice == '4':
            run_file('choose.py')
        elif choice == '5':
            run_file('clocks.py')
        elif choice == '6':
            run_file('draw.py')
        elif choice == '7':
            run_file('filez.py')
        elif choice == '8':
            run_file('flash.py')
        elif choice == '9':
            run_file('generator.py')
        elif choice == '10':
            run_file('guessing_game.py')
        elif choice == '11':
            run_file('guessing_game_gui.py')
        elif choice == '12':
            run_file('hangman.py')
        elif choice == '13':
            run_file('images.py')
        elif choice == '14':
            run_file('palindrome.py')
        elif choice == '15':
            run_file('rps.py')
        elif choice == '16':
            run_file('speed.py')
        elif choice == '17':
            run_file('tictactoe.py')
        elif choice == '18':
            run_file('todo.py')
        elif choice == '19':
            run_file('validate.py')
        elif choice == '20':
            run_file('wordcount.py')
        elif choice == '21':
            print("Exiting the program. Later Duder!")
            break
        else:
            print("Invalid Option. Please selecte from 1-21.")





# Run the program
main_menu()