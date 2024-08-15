#list, tiples and sets

#LIST: list is mutable, order is kept, can hold different data types, can be changed in place
l = ["bob", "alice", "jane"]
print(l[0])  #prints first element

#TUPLE: tuple is mutable, order is kept, can hold different data types, but can't be changed in place
print(l[0])
t = ("bob", "alice", "jane")
print(t[0])  #prints first element

#SET: set is unordered, unmutable, can hold different data types, elements in set are unique
print(t[0])
s = {"bob", "alice", "jane"}
print(s)
print(s)

l.append("john")
print(l)

l.remove("bob")
print(l)

s.add("Issa")
print(s)


