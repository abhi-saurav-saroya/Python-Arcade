import random


def intro() -> None:
    print("""
===================================
       COIN TOSS SIMULATOR
===================================

Flip a coin.

Will it be Heads or Tails?
""")


def toss_coin() -> str:
    return random.choice(["Heads", "Tails"])


def display_result(result: str) -> None:
    print(f"\nThe coin landed on: {result}")


def play_round() -> None:
    result = toss_coin()

    display_result(result)


def play_again() -> bool:
    while True:
        choice = input("\nToss again? (y/n): ").strip().lower()

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