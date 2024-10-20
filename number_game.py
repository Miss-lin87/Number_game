# this calles the text explaining the game and how it works
def start():
    print("Welcome to the numbers game. In this game you will guess what number the computer is thinking about \nEvery guess you will get to know if the number the computer is thinking about is higher or lower than your guess \nThe goal is to guess the number in as few guesses as possible")
    print("Lets start by picking a range of numbers for the computer")

# This allowes you yo select the range for the game, return both low and high end of the range
def rang():
    ran_low = int(input("Select starting value of the range: "))
    ran_hi = int(input("Select the ending value o the range: "))
    return ran_low, ran_hi

# This is the function for making guesses in the game
def guesses():
    guess = int(input("Please guess a number "))
    return guess

# This makes a comparison towards the target and returns if the target is higher, lower or if you win
def comparison(target, guess):
    if str(guess) > str(target):
        print("Try Again! You guessed too high.")
        return guess
    elif str(guess) < str(target):
        print("Try Again! You guessed too low.")
        return guess
    else:
        print("You sucessfully guessed the right number")
        return guess

# This is a test to validate if the selection is within the range selected in the start
def test_valid(ran_low, ran_hi, guess):
    if guess not in range(ran_low, ran_hi): print("The guess is outside of selected range \n"); test_valid(ran_low, ran_hi, guesses())
    else: return guess