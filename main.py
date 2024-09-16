import random

number = random.randint(1, 100)

user_input = None

while user_input != number:
    user_input = int(input("Guess a number between 1 and 100: "))

    if user_input < number:
        print("Guess higher")
    elif user_input > number:
        print("Guess lower")
    elif user_input == number:
        print("Congrats. You found it!")