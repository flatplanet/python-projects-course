import os
os.system("clear")
#print(sorted("dogs", reverse=True))
#print(sorted("god"))
#print(sorted("dogs") == sorted("god"))

# Function to check if two words are anagrams
def are_anagrams(word1, word2):
    # Decide if two words are anagrams?
    #sorted(john) == hjno
    return sorted(word1) == sorted(word2)

# Function to find all anagrams of a word from a list of dictionary words 
def find_anagrams(word, word_list):
    # conver word to lowercase
    word = word.lower()

    # Return a list of words that are anagrams of the input word
    return [w for w in word_list if are_anagrams(word, w.lower()) and w.lower() != word]


# Main Function
def anagram_solver():
    # Create a list of dictionary words to check against
    word_list = ["listen", "silent", "enlist", "tinsel", "google", "elder", "dog", "god", "evil", "vile", "live"]

    # Prompt the user
    word = input("Enter a word to find it's anagrams: ")

    # Find anagrams for the word
    anagrams = find_anagrams(word, word_list)

    # Output
    if anagrams:
        print(f'Anagrams of "{word}" are: {', '.join(anagrams)}')
    else:
        print(f'No anagrams found for word "{word}".')





# Run the thing
anagram_solver()