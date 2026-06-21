from number_guessing_user.game import play as number_guessing_user
from number_guessing_computer.game import play as number_guessing_computer
from hangman.game import play as hangman
from rock_paper_scissors.game import play as rock_paper_scissors
from dice_roll.game import play as dice_roll
from coin_toss.game import play as coin_toss
from word_scramble.game import play as word_scramble


GAMES = {
    "1": ("Number Guessing Game (You guess)", number_guessing_user),
    "2": ("Number Guessing Game (Computer guesses)", number_guessing_computer),
    "3": ("Hangman", hangman),
    "4": ("Rock Paper Scissors", rock_paper_scissors),
    "5": ("Dice Roll", dice_roll),
    "6": ("Coin Toss", coin_toss),
    "7": ("Word Scramble", word_scramble),
}


def display_menu() -> None:
    print("\n" + "=" * 40)
    print("        TERMINAL ARCADE")
    print("=" * 40)

    for key, (name, _) in GAMES.items():
        print(f"{key}. {name}")

    print("0. Exit")


def main() -> None:
    while True:
        display_menu()

        choice = input("\nSelect a game: ").strip()

        if choice == "0":
            print("\nThanks for playing!")
            break

        if choice in GAMES:
            _, game_function = GAMES[choice]
            print()
            game_function()
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()