# import sys
import random
import sys
from enum import Enum


class YZF(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


playagain = True

while playagain:

    stars = "********************"
    computer_choice = int(random.choice("123"))

    player_choice_input = input(
        "Make your choice\n1 for Rock\n2 for Paper\n3 for Scissors:\n\n"
    )
    player_choice = int(player_choice_input)

    if player_choice < 1 or player_choice > 3:
        print(f"{stars}")
        print("Please enter a number for 1 to 3")
        continue

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
    playagain_changer = input("Play Again Y fot play N for end game\n\n")
    if playagain_changer.lower() == "y":
        continue
    else:
        print("stop the game")
        playagain = False

sys.exit("By")
