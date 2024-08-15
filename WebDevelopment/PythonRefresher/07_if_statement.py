#if statements

day_of_week = input("What day of the week is it? ").lower()
if day_of_week == "tuesday" :
    print("Yay, it's Tuesday!")
elif day_of_week == "monday":
    print("Boo, it's Monday!")
else:
    print("Full speed ahead!")

#in keyword
friends = {"bob", "alice", "jane"}
abrood = {"bob", "anne"}

print("bob" in friends)

movies_watched = {"The Matrix", "The Matrix Reloaded", "The Matrix Revolutions"}
user_movies = input("Enter something you've watched recently: ")


if user_movies in movies_watched:
    print(f"I've watched {user_movies} too!")
else:
    print("I haven't watched that yet!")


#Magic Number

magic_number = 9

user_input = int(input("Enter a y if you want to play: "))

if user_input in ("Y","y"):
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == magic_number:
        print("You guessed correctly!")
    elif guess < magic_number:
        print("Your guess was too low!")
    elif guess > magic_number:
        print("Your guess was too high!")
    else:
        print("Sorry, you guessed incorrectly.")
else:
    print("Ok, maybe next time!")


