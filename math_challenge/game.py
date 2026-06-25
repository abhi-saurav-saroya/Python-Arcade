import random


def intro() -> None:
    print("""
===================================
         MATH CHALLENGE
===================================

Answer the math questions.
The game ends when you get one wrong.
""")


def generate_question() -> tuple[str, int]:
    operation = random.choice(["+", "-", "*", "/"])

    if operation == "+":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        answer = a + b

    elif operation == "-":
        a = random.randint(1, 100)
        b = random.randint(1, a)
        answer = a - b

    elif operation == "*":
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        answer = a * b

    else:  # division
        answer = random.randint(1, 12)
        b = random.randint(1, 12)
        a = answer * b

    question = f"{a} {operation} {b}"

    return question, answer


def play_round() -> int:
    streak = 0

    while True:
        question, answer = generate_question()

        try:
            guess = int(input(f"\n{question} = "))
        except ValueError:
            print("Please enter a number.")
            continue

        if guess == answer:
            streak += 1
            print("Correct!")
            print(f"Current streak: {streak}")
        else:
            print(f"Wrong! The answer was {answer}.")
            return streak


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
        streak = play_round()

        print(f"\nFinal streak: {streak}")

        if not play_again():
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    play()