import random

# List of words for the game
word_list = [
    "apple", "banana", "cherry", "orange", "grape",
    "lemon", "melon", "pear", "peach", "strawberry"
]


def select_random_word():
    #Selects a random word from the word_list.
    return random.choice(word_list)


def display_word(word, guessed_letters):
    #Displays the word with guessed letters filled in, others as underscores.
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()


def hangman():
    #Main function to run the Hangman game.
    print("Welcome to Hangman!")
    word_to_guess = select_random_word()
    print(word_to_guess)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6  # Adjust the maximum number of incorrect attempts allowed

    print("Guess the word:")
    while incorrect_guesses < max_attempts:
        print(display_word(word_to_guess, guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

        if all(letter in guessed_letters for letter in word_to_guess):
            print(display_word(word_to_guess, guessed_letters))
            print("Congratulations! You guessed the word correctly.")
            break

    if incorrect_guesses == max_attempts:
        print(
            f"Sorry, you've run out of attempts. The word was '{word_to_guess}'.")


if __name__ == "__main__":
    hangman()
