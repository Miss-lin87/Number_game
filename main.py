import number_game
from random import randint as random

# A tracker keeping track on the number of tries made
tries = 1

# this runs the game
def game():
    try:
        number_game.start()
        global tries
        ran_low, ran_hi = number_game.rang()
        target = random(ran_low, ran_hi)
        print("The computer has picked a target number")
        guess = number_game.comparison(target, number_game.test_valid(ran_low, ran_hi, number_game.guesses()))
        while guess != target:
            tries += 1
            guess = int(number_game.comparison(target, number_game.test_valid(ran_low, ran_hi, number_game.guesses())))
        else: return "It took you " + str(tries) + " tries to guess correct"
    except ValueError:
        print("Something went wrong. Starting over\n\n")
        game()

print(game())