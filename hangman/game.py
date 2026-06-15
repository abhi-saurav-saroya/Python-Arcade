import random


def intro() -> None:
    print("""
===================================
          HANGMAN GAME
===================================

Try to guess the hidden word.

Rules:
- Guess one letter at a time.
- You have 6 incorrect guesses.
- Only English letters are allowed.
""")


def load_words() -> list[str]:
    with open("words.txt", "r") as file:
        return [
            word.strip().lower()
            for word in file
            if word.strip().isalpha()
        ]


def get_letter(guessed_letters: set[str]) -> str:
    while True:
        letter = input("\nEnter a letter: ").strip().lower()

        if len(letter) != 1:
            print("Please enter exactly one letter.")
            continue

        if not letter.isalpha():
            print("Please enter a valid letter.")
            continue

        if letter in guessed_letters:
            print("You already guessed that letter.")
            continue

        return letter


def display_word(secret_word: str, guessed_letters: set[str]) -> None:
    displayed = []

    for letter in secret_word:
        if letter in guessed_letters:
            displayed.append(letter)
        else:
            displayed.append("_")

    print("\nWord: " + " ".join(displayed))


def is_word_guessed(secret_word: str, guessed_letters: set[str]) -> bool:
    for letter in secret_word:
        if letter not in guessed_letters:
            return False

    return True


def play_round() -> None:
    words = load_words()

    secret_word = random.choice(words)

    guessed_letters = set()

    remaining_attempts = 6

    print(
        f"\nThe word contains "
        f"{len(secret_word)} letters."
    )

    while remaining_attempts > 0:
        display_word(secret_word, guessed_letters)

        print(f"Incorrect guesses left: {remaining_attempts}")

        letter = get_letter(guessed_letters)

        guessed_letters.add(letter)

        if letter in secret_word:
            print("Correct!")

            if is_word_guessed(secret_word,guessed_letters):
                print("\nCongratulations!")
                print(f"You guessed the word: {secret_word}")
                return

        else:
            remaining_attempts -= 1
            print("Wrong guess!")

    print("\nGame Over!")
    print(f"The word was: {secret_word}")


def play_again() -> bool:
    while True:
        choice = input("\nWould you like to play again? (y/n): ").strip().lower()

        if choice in ("y", "yes"):
            return True

        if choice in ("n", "no"):
            return False

        print("Please enter y or n.")


def play() -> None:
    intro()

    while True:
        play_round()

        if not play_again():
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    play()