"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

    
def start_game():
    dashes = ("-" * 36)
    print("\n{}\nWelcome to the Number Guessing Game!\n{}\n".format(dashes, dashes))
    play_again = "y"
    while play_again.lower() == "y":
        number = random.randint(0,9)
        number = int(number + 1)
        
# ====> REMOVE THESE TWO LINES BEFORE SUBMITTING PROJECT!!
        ##print("The number is {}.".format(number))
    
        guess = input("Guess a number between 1-10.  ")
        guess = int(guess)
        print(guess)
        guess_count = 0
        high_score = 10
        guess_count = int(guess_count + 1 )
        while guess != number:
            if guess > 10 or guess < 1:
                guess = input("Your guess must be between 1-10. Please try again.  ")
                guess = int(guess)
                guess_count += 1
            elif guess > number:
                guess = input("It's lower!! Guess again:  ")
                guess = int(guess)
                guess_count += 1
            elif guess < number:
                guess = input("It's higher!! Guess again:  ")
                guess = int(guess)
                guess_count += 1
        print("You got it! It took you {} guesses.  Thanks for playing!!".format(guess_count))
        if guess_count < high_score:
            high_score = guess_count
        play_again = input("\nWould you like to play again? Y/N  ")
        if play_again.lower() == "y":
            print("\nThe high score so far is {}. Can you beat it?\n".format(high_score))
        else:
            print("\nThank you for playing! The game is now closing.\n")

start_game()

