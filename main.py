from number_guessing_user.game import play as number_guessing


GAMES = {
    "1": ("Number Guessing Game", number_guessing),
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