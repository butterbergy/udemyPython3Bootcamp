age = input("How old are you?\n")
if age:
    age = int(age)
    if age >= 21:
        print("You can enter and drink")
    elif age >= 18:
        print("You can enter with a wristband")
    else:
        print("Sorry you are too young")
else:
    print("Please enter your age as an int")
