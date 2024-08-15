

#Strings 
name = "Issa"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)


longer_phrase = "Hello, {}. Today is {}"
with_names = longer_phrase.format(name, "Monday")
print(with_names)


