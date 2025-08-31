import random

magic_number = random.randrange(1, 51)
counter = 0
max_guesses = 5

guess = int(input("Guess the number I'm thinking of: "))

while guess != magic_number and counter < max_guesses - 1:
    counter += 1
    if guess < magic_number:
        guess = int(input("Too low! Guess again: "))
    elif guess > magic_number:
        guess = int(input("Too high! Guess again: "))

counter += 1  # count the final guess
if guess == magic_number:
    print("You got it in {} guesses! It was {}.".format(counter, magic_number))
else:
    print("Out of guesses! The number was {}.".format(magic_number))

