import random

def select_random_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'developer', 'software']
    return random.choice(words)

def display_current_state(word, correct_guesses):
    display = ''
    for letter in word:
        if letter in correct_guesses:
            display += letter
        else:
            display += '_'
    return display

def hangman_game():
    word = select_random_word()
    correct_guesses = []
    incorrect_guesses = []
    max_incorrect = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while len(incorrect_guesses) < max_incorrect:
        current_state = display_current_state(word, correct_guesses)
        print(f"Word: {current_state}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Guesses left: {max_incorrect - len(incorrect_guesses)}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter.")
            continue

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            correct_guesses.append(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses.append(guess)

        if all(letter in correct_guesses for letter in word):
            print(f"Congratulations! You've guessed the word '{word}'!")
            break
    else:
        print(f"Out of guesses! The word was '{word}'. Better luck next time.")

if __name__ == "__main__":
    hangman_game()
