import random


def intro() -> None:
    print("""
===================================
         DICE ROLLER
===================================

Roll a six-sided die.

Try your luck!
""")


def roll_dice() -> int:
    return random.randint(1, 6)


def display_result(result: int) -> None:
    print(f"\nYou rolled: {result}")


def play_round() -> None:
    result = roll_dice()

    display_result(result)


def play_again() -> bool:
    while True:
        choice = input("\nRoll again? (y/n): ").strip().lower()

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