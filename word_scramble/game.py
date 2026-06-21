import random


WORDS = [
    "python",
    "computer",
    "keyboard",
    "programming",
    "developer",
    "variable",
    "function",
    "algorithm",
]


def intro() -> None:
    print("""
===================================
         WORD SCRAMBLE
===================================

Unscramble the word.
""")


def get_scrambled_word(word: str) -> str:
    letters = list(word)

    random.shuffle(letters)

    return "".join(letters)


def play_round() -> None:
    word = random.choice(WORDS)

    scrambled_word = get_scrambled_word(word)

    print(f"\nScrambled word: {scrambled_word}")

    guess = input("Your guess: ").strip().lower()

    if guess == word:
        print("Correct!")
    else:
        print(f"Wrong! The word was '{word}'.")


def play_again() -> bool:
    while True:
        choice = input("\nPlay again? (y/n): ").strip().lower()

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