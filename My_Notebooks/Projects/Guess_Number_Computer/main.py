import random

x = int(input("Enter x: "))


def computer_guess(x):
    low = 1
    high = x

    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(
            f"is {guess} guess too high(H), too low(L) or correct (C)??").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            lower = guess + 1

    print(f'Congratulation! the computer guessed your number {guess}')


computer_guess(x)
