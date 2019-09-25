import random

random_num = random.randint(1, 10)
picked_num = int(input("Pick a number between 1 and 10.\n"))

while picked_num != random_num:
    if picked_num > random_num:
        print("Too High! Try again")
    else:
        print("Too Low! Try again")
    picked_num = int(input("Pick a number between 1 and 10.\n"))

print("Congrats, you win!!!")
