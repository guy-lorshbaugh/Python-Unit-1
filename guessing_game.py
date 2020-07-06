import random
   
def start_game():
    dashes = ("-" * 36)
    print("\n{}\nWelcome to the Number Guessing Game!\n{}\n".format(dashes, dashes))
    play_again = "y"
    high_score = 10
    while play_again.lower() == "y":
        number = random.randint(1,10)
        guess = input("Guess a number between 1-10.  ")
        guess_count = 1
        try:
            guess = int(guess)
        except ValueError as err:
            print("Invalid entry.  Please enter a numeral value between 1-10.")
        else:
            while guess != number:
                if not (1 <= guess <= 10):
                    guess = input("Your guess must be between 1-10. Please try again.  ")
                else:
                    word = 'lower' if guess > number else 'higher'
                    guess = input(f"It's {word}!! Guess again:  ")
                guess = int(guess)
                guess_count += 1
            print(f"You got it! It took you {guess_count} guesses.  Thanks for playing!!")
            if guess_count < high_score:
                high_score = guess_count
            play_again = input("\nWould you like to play again? Y/N  ").lower()
            if play_again == "y":
                print("\nThe high score so far is {}. Can you beat it?\n".format(high_score))
            else:
                print("\nThank you for playing! The game is now closing.\n")
            
start_game()