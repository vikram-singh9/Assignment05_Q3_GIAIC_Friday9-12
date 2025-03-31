import random

# List of words to choose from
words = ["python", "programming", "computer", "algorithm", "database", "network", "software"]

def get_word():
    return random.choice(words).lower()

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]

def play_hangman():
    word = get_word()
    word_letters = set(word)  # letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # letters guessed by the user

    tries = 6  # number of tries before game over

    # getting user input
    while len(word_letters) > 0 and tries > 0:
        print("\nYou have", tries, "tries left.")
        print("Used letters:", " ".join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(display_hangman(tries))
        print("Current word:", " ".join(word_list))

        guess = input("Guess a letter: ").lower()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                tries -= 1
                print("Letter is not in the word.")

        elif guess in used_letters:
            print("You have already used that letter. Please try again.")

        else:
            print("Invalid character. Please try again.")

    # gets here when len(word_letters) == 0 OR tries == 0
    if tries == 0:
        print(display_hangman(0))
        print("You died! The word was", word)
    else:
        print("Congratulations! You guessed the word", word, "!!")

print("Welcome to Hangman!")
while True:
    play_hangman()
    play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        print("Thanks for playing!")
        break
