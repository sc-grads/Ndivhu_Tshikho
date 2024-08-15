def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(1, 2)  # prints "1 + 2 = 3"


def say_hello(name, surname):
    print(f"Hello {name}{surname}")

say_hello(name="Issa", surname=" Tshikovhokhovho")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)

    else:
        print("you can't divide by zero")


divide(dividend=10, divisor=0)
