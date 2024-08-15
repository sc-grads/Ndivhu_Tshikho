#loops

magic_number = 9
user_input = input("Would you like to play? (Y/n) ")


while user_input != "n":
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == magic_number:
        print("You guessed correctly!")
        break
    elif guess < magic_number:
        print("Your guess was too low!")
    elif guess > magic_number:
        print("Your guess was too high!")
    else:
        print("Sorry, you guessed incorrectly.")

