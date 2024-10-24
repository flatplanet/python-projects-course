import time
import random
import os

# Clear the screen
os.system("clear")


# List of sentences for the typing
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an easy to learn programming language.",
    "Artificial intelligence will shape the future of technology.",
    "Typing speed tests are quite stupid, and a waste of time!",
    "Consistent practice is key to mastering any skill."
]


# Function to calculate words per minute (WPM)
def calculate_wpm(start_time, end_time, typed_text):
    # calculate the time in seconds that it took to finish
    time_taken = end_time - start_time # in seconds
    # Calculate the number of words
    num_words = len(typed_text.split())
    # Calculate WPM words per minute
    wpm = (num_words / time_taken) * 60 # words per minute formula
    # return the results
    return(round(wpm, 2))




# Function to run the typing speed test
def typing_speed_test():
    # Choose a random sentence from our list
    sentence = random.choice(sentences)

    print("\n--- Typing Speed Test ---")
    print("Type the following sentence as fast as you can:")
    print(f"\n{sentence}\n")

    # Tell the user to hit enter to start 
    input("Press Enter when you're ready to start...")

    # Start the timer
    start_time = time.time()

    # Prompt the user to start typing
    typed_text = input("\nStart typing here: (hit enter when finished)\n")

    # Get the end time
    end_time = time.time()

    # Calculate WPM (words per minute)    
    wpm = calculate_wpm(start_time, end_time, typed_text)

    # Output the results / check for errors
    if typed_text == sentence:
        print(f"Great job! Your typing speed is {wpm} words per minute!")
    else:
        print(f"Your typing speed is {wpm} words per minute, but there were some mistakes in your typing.")






# Main function
def main():
    while True:
        # clear the screen
        os.system("clear")
        # Start the test
        typing_speed_test()
        # Ask user to try again
        retry = input("\nWould you like to try again? (y/n)?").lower()
        # Logice to determine what they selected y/n
        if retry != "y":
            print("Thanks for using the Typing Speed test!  Later Duder!")
            break








# Run our app
main()

