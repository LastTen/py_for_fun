# import sys
import random
from enum import Enum


class YZF(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


stars = "********************"


def game():
    try:
        player_choice_input = input(
            "Make your choice\n1 for Rock\n2 for Paper\n3 for Scissors:\n"
        )
        player_choice = int(player_choice_input)
        computer_choice = int(random.choice("123"))

    except ValueError:
        print(f"{stars}")
        print("Invalid input. Please enter a number.")
        game()

    if player_choice < 1 or player_choice > 3:
        print(f"{stars}")
        print("Please enter a number for 1 to 3")
        game()

    print(
        f"\nYour choice is {str(YZF(player_choice)).replace('YZF.', '')}\n"
        + f"Computer choice is {str(YZF(computer_choice)).replace('YZF.', '')}\n"
    )

    if player_choice == computer_choice:
        print("😉It's a tie!")
    elif player_choice == 1 and computer_choice == 3:
        print("🎉You won!🎉")
    elif player_choice == 2 and computer_choice == 1:
        print("🎉You won!🎉")
    elif player_choice == 3 and computer_choice == 2:
        print("🎉You won!🎉")
    else:
        print("You lost!. won python 🐍")

    print(f"{stars}")
    print("Play again")


while True:
    game()
