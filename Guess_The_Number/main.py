import random

# Welcome Banner
print("""

##########################################################################
                    WELCOME TO THE GUESSING GAME!
Please pick two numbers to represent the range that your guess will be in.
The first will be the lower range, and the latter will be the upper range.
##########################################################################
"""
      )

# Generating the range the guesses will be in
lower_bound = int(input("First number: "))
upper_bound = int(input("Last number: "))

# Generating a number to guess within bounds
correct_number = random.randint(lower_bound, upper_bound)

# Attempt system
print("And how many attempts would you like?")
total_attempts = int(input())

# Gameplay Loop
incorrect_guess = True

while True:
    print("What is your guess?")
    guess = int(input())
