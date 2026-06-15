import random


def intro() -> None:
    print("""
===================================
      NUMBER GUESSING GAME
===================================

I will think of a random number.
Your job is to guess it!

Difficulty Levels:
1. Easy   (1 - 10)
2. Medium (1 - 100)
3. Hard   (1 - 1000)
""")


def select_level() -> int:
    while True:
        choice = input(
            "Choose difficulty (1, 2, or 3): "
        ).strip()

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        choice = int(choice)

        if choice in (1, 2, 3):
            return choice

        print("Invalid choice. Please select 1, 2, or 3.")


def get_highest_val(level: int) -> int:
    levels = {
        1: 10,
        2: 100,
        3: 1000
    }

    return levels[level]


def get_guess(max_value: int) -> int:
    while True:
        guess = input(
            f"Enter your guess (1-{max_value}): "
        ).strip()

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if 1 <= guess <= max_value:
            return guess

        print(
            f"Number must be between 1 and {max_value}."
        )


def play_round() -> None:
    level = select_level()

    highest_val = get_highest_val(level)

    secret_number = random.randint(1, highest_val)

    attempts = 0

    print(
        f"\nI have selected a number between "
        f"1 and {highest_val}."
    )

    while True:
        guess = get_guess(highest_val)
        attempts += 1

        if guess == secret_number:
            print("\n🎉 Congratulations!")
            print(f"You guessed the number in {attempts} attempt(s).")
            break

        difference = abs(secret_number - guess)
        if difference <= 3:
            print("Very close!")
        elif difference <= 10:
            print("Getting warmer!")

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")


def play_again() -> bool:
    while True:
        choice = input(
            "\nWould you like to play again? (y/n): "
        ).strip().lower()

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