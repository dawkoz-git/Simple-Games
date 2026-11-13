import functions
import random

# Welcome Banner
print("""

##########################################################################
                    WELCOME TO THE GUESSING GAME!
Your objective is to guess the number within a certain number of attempts!
                            Good luck.
##########################################################################
"""
      )
# Setting up the game loop boolean
incorrect_guess = True

while incorrect_guess:

    # Difficulty settings
    print("Do you want to play on easy, medium, or hard difficulty? (1, 2, or 3)")
    print("""
    [1] Easy - 6 guesses for a number between 1-100
    [2] Medium - 13 guesses for a number between 1-10,000
    [3] Hard - 20 guesses for a number between 1-100,000,000
  
    """)

    difficulty = int(input())

    diff_validity = True

    # Looping difficulty to ensure valid option is selected
    while diff_validity:
        if difficulty not in (1, 2, 3):
            print("That's an invalid option! Please pick 1, 2, or 3.")
            difficulty = int(input())

        if difficulty == 1 or 2 or 3:
            diff_validity = False

    # Getting values from functions file to use
    attempts = functions.diffsettings(difficulty)[0]
    upper_bound = functions.diffsettings(difficulty)[1]

    correct_number = random.randint(1, upper_bound)

    # Initialising Game Loop
    print(f"Please pick a number between 1 and {upper_bound}")

    user_guess = int(input())

    while user_guess != correct_number:
        attempts = attempts - 1
        if user_guess > upper_bound or user_guess < 1:
            print(f"That's not within bounds! It must be between 1 and {upper_bound}")
            user_guess = int(input())
        elif user_guess > correct_number:
            print("Good guess! Your guess is too high. Try again!")
            user_guess = int(input())
        elif user_guess < correct_number:
            print("Good guess! Your guess is too low. Try again!")
            user_guess = int(input())

    print(f"Well done! You guessed the number in {attempts} attempts!")
