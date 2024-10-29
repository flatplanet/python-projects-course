import os
import random



'''
num = random.random()
print(num)
print(num < 0.2)
'''

# function to display the intro text
def diplay_inro():
    print("Welcome to the big time adventure game!")
    print("You're on a quest to rescue the princes in the castle.")
    print("Navigate carefully using directions: N (north), S (south), E (east), W (west).")
    print("Watch out for pits!  They could pop up anywhere...")
    print("Good Luck on your adventure!!\n")



# Function to check for danger/pit
def check_for_pit():
    # Set random level for pit falling - 10%
    # Generate a random float between 0 and 1 .05, .2, .9
    return random.random() < 0.10  
    # True for pit, False for No Pit





# Function for the game
def adventure_game():
    # Clear the screen
    os.system("clear")
    # Call the display menu thing
    diplay_inro()
    #Keep track of the steps
    steps = 0

    # game loop
    while True:
        direction = input("Choose a direction (N/S/E/W): ").upper()

        # check for errors
        if direction not in ['N', 'S', 'E', 'W']:
            print("Invalid Direction, please choose N, S, E, or W.")
            continue

        # increase the step cout
        steps += 1

        # Check if player fell into the pit
        if check_for_pit():
            print(f"Oh No! You chose {direction} and fell into a pit! Game over!")
            break

        # Check for 5 steps
        if steps >= 5:
            print(f"Congrats! After {steps} steps, you have reached the castle and rescued the princess! You Win!")
            break
        else:
            print(f"You moved {direction}. Keep going!")





# Main function
def main():
    while True:
        # Call the game function
        adventure_game()
        # ask to play again
        replay = input("\nWould you like to play again (y/n): ").lower()
        # Logic to determine if they want to play again
        if replay != 'y':
            print("Thanks for playing! Later duder!")
            break




# Run the game
main()