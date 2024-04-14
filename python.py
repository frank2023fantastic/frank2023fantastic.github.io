import random

random_number = random.randint(1, 100)
i = 5
while i != 0:
    y = int(input("guess a number({i}, chances)"))
    if y == random_number:
        print("you are correct!")
        i = 0
    if y >= random_number:
        print("too big, guess again!")
    if y <= random_number:
        print("too small, guess again!")
    i = i - 1
print("try again!")
