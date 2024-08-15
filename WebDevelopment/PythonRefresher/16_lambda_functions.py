#lambda functions
add = lambda x: x + 10

#calling a function
print(add(1))


def double(x):
    return x * 2

seq = [1, 2, 3, 4, 5]
doubled = [double(x) for x in seq]
print(doubled)
###################################
#the map function applies a function to every item in an iterable.
#It returns an iterator object which is an iterable.
#The map function does not change the original iterable.
#The map function is lazy, meaning it does not evaluate the iterator until the iterable is iterated over.
#The map function is a high order function, meaning it takes another function as an argument.
#The map function is often used in combination with list comprehension to create a list.

doubled = map(lambda x: x * 2, seq)
doubled_list = list(doubled) #convert iterable to list
print(doubled_list)
