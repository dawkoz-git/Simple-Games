import functions

# Welcome Banner
print("""

##########################################################################
                    WELCOME TO THE GUESSING GAME!
Your objective is to guess the number within a certain number of attempts!
                            Good luck.
##########################################################################
"""
      )
# Setting up the gameloop
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




