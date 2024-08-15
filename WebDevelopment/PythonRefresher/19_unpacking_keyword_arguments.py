def named(**kwargs):
    print(kwargs)

named(first = 'Guido', last = 'Van Rossum')

#################################################

def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 2, 3, first=4, second=5)

