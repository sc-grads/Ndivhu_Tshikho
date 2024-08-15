def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total



multiply(1, 2, 3, 4)


def add(x, y):
    return x + y

nums = [3, 4]
print(add(*nums))

#####################################

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."
    

print(apply(1, 2, 3, 4, operator = "*"))

