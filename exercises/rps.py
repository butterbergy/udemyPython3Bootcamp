import random

print("...rock...")
print("...paper...")
print("...scissors...")

you = input("Your choice: ")

moves = ["rock", "paper", "scissors"]
computer = moves[random.randint(0, 2)]
print(f"The computer chose: {computer}")

if you == computer:
    print("tie game")
elif you == "rock":
    if computer == "scissors":
        print("you win")
    else:
        print("computer wins")
elif you == "scissors":
    if computer == "rock":
        print("computer wins")
    else:
        print("you win")
elif you == "scissors":
    if computer == "rock":
        print("you win")
    else:
        print("computer wins")
else:
    print("Something went wrong")
