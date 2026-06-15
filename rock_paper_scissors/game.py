import random


def intro() -> None:
    print("""
===================================
      ROCK PAPER SCISSORS
===================================

Choose:
1. Rock
2. Paper
3. Scissors

Beat the computer and win!
""")


def get_player_choice() -> int:
    while True:
        choice = input("Choose (1, 2, or 3): ").strip()

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        choice = int(choice)

        if choice in (1, 2, 3):
            return choice

        print("Invalid choice. Please select 1, 2, or 3.")


def get_choice_name(choice: int) -> str:
    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }

    return choices[choice]


def get_computer_choice() -> int:
    return random.randint(1, 3)


def determine_winner(player_choice: int,computer_choice: int) -> str:
    if player_choice == computer_choice:
        return "tie"

    winning_combinations = {
        (1, 3),
        (2, 1),
        (3, 2)
    }

    if (player_choice, computer_choice) in winning_combinations:
        return "player"

    return "computer"


def display_result(player_choice: int, computer_choice: int, winner: str) -> None:
    print(f"\nYou chose: {get_choice_name(player_choice)}")

    print(f"Computer chose: {get_choice_name(computer_choice)}")

    if winner == "tie":
        print("\nIt's a tie!")

    elif winner == "player":
        print("\nYou win!")

    else:
        print("\nComputer wins!")


def play_round() -> None:
    player_choice = get_player_choice()

    computer_choice = get_computer_choice()

    winner = determine_winner(player_choice, computer_choice)

    display_result(player_choice, computer_choice, winner)


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