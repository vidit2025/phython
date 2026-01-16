# main.py
# Goal: To understand Python data structures (List) using a simple guessing game

import random

# List of numbers given to Harsh
numbers = [10, 20, 30, 40, 50, 60, 70]

# Judge randomly chooses a number from the list
chosen_number = random.choice(numbers)

print("Welcome Harsh!")
print("You are participating in a quiz competition.")
print("Here is the list of numbers:", numbers)

# Harsh guesses a number
guess = int(input("Guess the number chosen by the judge: "))

# Comparing the guessed number with the chosen number
if guess > chosen_number:
    print("Your guessed number is higher than the original number.")
elif guess < chosen_number:
    print("Your guessed number is smaller than the original number.")
    print("Best of luck!")
else:
    print("Congratulations! You guessed the correct number 🎉")
