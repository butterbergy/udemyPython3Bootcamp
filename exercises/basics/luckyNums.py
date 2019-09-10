for i in range(1, 21):
    if i == 4 or i == 13:
        phrase = "unlucky"
    elif i % 2 == 0:
        phrase = "even"
    else:
        phrase = "odd"
    print(f"{i} is {phrase}")
