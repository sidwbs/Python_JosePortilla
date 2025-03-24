import random


def play():

    my_move = input(
        "What's your choice? 'r' for rock, 'p' for paper, 's' for scissor: ")
    computers_move = random.choice(['r', 'p', 's'])
    if my_move == computers_move:
        print("Draw!")

    if is_win(my_move, computers_move) == True:
        print("You Won!")

    elif is_win(my_move, computers_move) == False:
        print("Computer Won!")
    print(f"Computers move: {computers_move}\n Your move: {my_move}")


def is_win(my_move, computers_move):
    if (computers_move == 'p' and my_move == 'r') or (computers_move == 's' and my_move == 'p') or (computers_move == 'r' and my_move == 's'):
        return False
    else:
        return False


play()
3
