import random
number_to_be_guessed = random.randint(1, 1000)
number_to_be_guessed = 0< 50

guess = int(input("Guess a number between 1 and 1000:"))
guess = int(input(" try again Guess a number between 1 and 1000:"))
guess = int(input(" last chance Guess a number between 1 and 1000:"))
number_to_be_guesses = 0<50
if guess == number_to_be_guessed:
    print("you got it right")
else:
    print("Try again later your money is gone you could not guess", number_to_be_guessed)