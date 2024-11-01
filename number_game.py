import time

def start():
    """This calles the text explaining the game and how it works"""
    print("Welcome to the numbers game. In this game you will guess what number the computer is thinking about \nEvery guess you will get to know if the number the computer is thinking about is higher or lower than your guess \nThe goal is to guess the number in as few guesses as possible")
    print("Lets start by picking a range of numbers for the computer")

def rang(ran_low=0, ran_hi=0):
    """This allowes you yo select the range for the game, return both low and high end of the range"""
    try:
        ran_low = int((input("Select starting value of the range: ")))
        ran_hi = int((input("Select the ending value of the range: ")))
        return ran_low, ran_hi
    except ValueError:
        print("That was not a valid number, try again")
        return rang()

def guesses():
    """This is the function for making guesses in the game"""
    guess = int(input("Please guess a number "))
    return guess

def comparison(target, guess):
    """This makes a comparison towards the target and returns if the target is higher, lower or if you win"""
    if str(guess) > str(target): print("Try Again! You guessed too high."); return guess
    elif str(guess) < str(target): print("Try Again! You guessed too low."); return guess
    else: print("You sucessfully guessed the right number") ;return guess

def test_valid(ran_low, ran_hi, guess):
    """This is a test to validate if the selection is within the range selected in the start."""
    try:
        if guess not in range(ran_low, ran_hi): print("The guess is outside of selected range \n"); return test_valid(ran_low, ran_hi, guesses())
        else: return guess
    except ValueError: print("The guess must be a number. Please try again"); return test_valid(ran_low,ran_hi,guesses())

def wait(x):
    """Simpel function to sleep X minutes"""
    time.sleep(x)
    return

def progress_bar():
    print("Wait while the result is checking")
    x = 1
    while x < 6:
        wait(0.25)
        print("Loading " + str(x*20) + "%")
        x += 1