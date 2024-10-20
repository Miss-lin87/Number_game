import number_game
from random import randint as random

tries = 1

def game():
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

print(game())