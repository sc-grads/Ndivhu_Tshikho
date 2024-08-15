def hello():
    print("Hello")

hello()


def user_age_in_seconds():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    age_in_seconds = age * 365 * 24 * 60 * 60
    print("{} is {} seconds old.".format(name, age_in_seconds))

user_age_in_seconds()



