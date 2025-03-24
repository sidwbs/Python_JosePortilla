import random

x = int(input("Enter x: "))
random_number = random.randint(1, x)


def guess(x):
    my_guess = None
    while my_guess != random_number:
        my_guess = int(input(f"Guess a number between 1 and {x}: "))
        if my_guess < random_number:
            print("Sorry guess again!. You guessed too low")
        elif my_guess > random_number:
            print("Sorry guess again! You guessed too high")

    print(
        f"Congratulations! you guessed the Number {random_number} correctly!")


guess(x)
