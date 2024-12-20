#two.py

import one

print("Top level in two.py")

one.func()

if __name__ == "__name__":
	print("two.py is being run directly!")

else:
	print("one.py has been imported!")