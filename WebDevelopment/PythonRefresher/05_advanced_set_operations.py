#Advanced set operations 

friends = {"bob", "alice", "jane"}
abrood = {"bob", "anne"}

local_friends = friends.difference(abrood)
print(local_friends)

local1 = {"rolf"}
abrood1 = {"issa", "lerato"}

friends1 = local1.union(abrood1)
print(friends1)

both = friends.intersection(abrood)
print(both)



