import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(words)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    user_input = input("Choose a word: ")

    if user_input in alphabets:
        if user_input in used_letters:
            print("Letter already used. Choose something else.")
        else:
            used_letters.add(user_input)

    else:
        print("Not a valid letter. Choose again!")
