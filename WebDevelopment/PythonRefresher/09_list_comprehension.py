numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled = [num * 2 for num in numbers]

print(doubled)

friends = ["Jim", "Karen", "Kevin"]
starts_k = []

# for friend in friends:
#     if friend.startswith("K"):
#         starts_k.append(friend)

starts_k = [friend for friend in friends if friend.startswith("K")]

print(starts_k)

