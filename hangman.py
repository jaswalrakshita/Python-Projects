import random

# List of words for the game
words = ['red', 'yellow', 'green', 'pink', 'white', 'black']

# Randomly choose a word from the list
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]  # Create a list of underscores to represent the word
print(word_display)

attempts = 8  # Number of attempts allowed

print("Welcome to Hangman Game!")

# The game continues until the word is guessed or the player runs out of attempts
while attempts > 0 and '_' in word_display:
    print("\n" + ''.join(word_display))  # Display the current state of the word
    guess = input("Guess a letter:\n").lower()  # Get the guessed letter and convert it to lowercase

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        # Reveal the guessed letter in the word display
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess  # Update the display with the correct guess
        print(f"Good guess! The letter '{guess}' is in the word.")
    else:
        # If the letter is not in the word, reduce the attempts
        print(f"That letter '{guess}' doesn't appear in the word!")
        attempts -= 1
        print(f"Remaining attempts: {attempts}")

    # Check if the word has been fully guessed
    if '_' not in word_display:
        print("\nYou guessed the word!")
        print(''.join(word_display))
        print("You survived!")
        break

# If the player runs out of attempts, show the loss message
if attempts == 0:
    print(f"\nAttempts finished. The word was: {chosen_word}")
    print("You Lost !!!!!")
