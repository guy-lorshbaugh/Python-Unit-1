import random
   
def start_game():
    dashes = "-" * 36
    print("\n{}\nWelcome to the Number Guessing Game!\n{}\n".format(dashes, dashes))
    play_again = "y"
    high_score = 10
    while play_again.lower() == "y":
        number = random.randint(1,10)
        guess_count = 1
        guess = None
        while guess != number:
            guess = input("Guess a number between 1-10.  ")
            try:  
                guess = int(guess)
            except ValueError:
                print("Invalid entry.  Please enter a numeral value between 1-10.")
            else:
                if not (1 <= guess <= 10):
                    print("Your guess must be between 1-10. Please try again.  ")
                elif guess == number:
                    print("You got it! It took you {} guesses.  Thanks for playing!!".format(guess_count))
                else:
                    word = 'lower' if guess > number else 'higher'
                    print("It's {}!! Guess again:  ".format(word))
                    guess_count += 1
        if guess_count < high_score:
            high_score = guess_count
        play_again = input("\nWould you like to play again? Y/N  ").lower()
        if play_again == "y":
            print("\nThe high score so far is {}. Can you beat it?\n".format(high_score))
        else:
            dashes2 = ("-" * 47)
            print("\n{}\nThank you for playing! The game is now closing.\n{}\n".format(dashes2,dashes2))

start_game()