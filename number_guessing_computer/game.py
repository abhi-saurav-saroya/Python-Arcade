import random

def intro() -> None:
    print("""
===================================
    COMPUTER GUESSING GAME
===================================

Think of a number and I will try
to guess it!

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


def get_response() -> str:
    while True:
        response = input(
            "Is my guess too high (h), "
            "too low (l), or correct (c)? "
        ).strip().lower()

        if response in ("h", "l", "c"):
            return response

        print("Please enter h, l, or c.")


def play_round() -> None:
    level = select_level()

    highest_val = get_highest_val(level)

    low = 1
    high = highest_val

    attempts = 0

    print(
        f"\nThink of a number between "
        f"1 and {highest_val}."
    )

    input("Press Enter when ready...")

    while low <= high:
        guess = random.randint(low, high)

        attempts += 1

        print(f"\nMy guess is: {guess}")

        response = get_response()

        if response == "c":
            print("\n🎉 I guessed it!")
            print(
                f"I found your number in "
                f"{attempts} attempt(s)."
            )
            return

        if response == "h":
            high = guess - 1

        elif response == "l":
            low = guess + 1

    print(
        "\nHmm... your answers seem "
        "to be inconsistent."
    )


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