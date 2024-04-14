import random

random_number = random.randint(1, 100)
i = 20
w = 0
while i != 0:
	y = int(input(f"Win time: {w} Guess a number: "))
	if y > random_number:
		print("too big, guess again!")
	if y < random_number:
		print("too small, guess again!")
	i = i - 1
	if y == random_number:
		print("you are correct!")
		i = 20
		w = w+1
		random_number = random.randint(1, 1000)
print("try again!")
