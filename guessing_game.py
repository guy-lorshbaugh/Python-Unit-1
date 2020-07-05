import random

    
def start_game():
    dashes = "-" * 36
    print("\n{}\nWelcome to the Number Guessing Game!\n{}\n".format(dashes, dashes))
    play_again = "y"
    while play_again == "y":
        number = random.randint(1, 10)
                
# ====> REMOVE THESE TWO LINES BEFORE SUBMITTING PROJECT!!
        ##print("The number is {}.".format(number))
    
        guess = int(input("Guess a number between 1-10.  "))
        print(guess)
        guess_count = 1
        high_score = 10
        while guess != number:
            if not (1 <= guess <= 10):
                guess = input("Your guess must be between 1-10. Please try again.  ")
            else:
                word = 'lower' if guess > number else 'higher'
                guess = input(f"It's {word}!! Guess again:  ")
            guess = int(guess)
            guess_count += 1
        print(f"You got it! It took you {guess_count} guesses.  Thanks for playing!!")
        high_score = min(guess_count, high_score)
        play_again = input("\nWould you like to play again? Y/N  ").lower()
        if play_again == "y":
            print("\nThe high score so far is {}. Can you beat it?\n".format(high_score))
        else:
            print("\nThank you for playing! The game is now closing.\n")

start_game()

