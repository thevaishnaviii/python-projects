'''
1 for snake
-1 for water
0 for gun
'''

import random

computer = random.choice([-1, 0, 1])

yourstr = input("Enter your choice (snake/water/gun): ").lower()
yourdict = {"snake": 1, "water": -1, "gun": 0}
reversedict = {1: "snake", -1: "water", 0: "gun"}

if yourstr not in yourdict:
    print("Invalid input!")
    exit()

you = yourdict[yourstr]

print(f"\nComputer chose: {reversedict[computer]}")
print(f"You chose: {reversedict[you]}\n")

if computer == -1 and you == 1:
    print("You win!")
elif computer == 1 and you == 0:
    print("You win!")
elif computer == 0 and you == -1:
    print("You win!")
elif computer == you:
    print("It's a tie!")
else:
    print("You lose!")