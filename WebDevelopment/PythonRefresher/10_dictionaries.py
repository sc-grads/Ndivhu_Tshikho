friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friend_ages["Bob"] = 20
print(friend_ages["Rolf"])

friend_ages["Rolf"] = 21
print(friend_ages["Rolf"])

print(friend_ages)

print(friend_ages.keys())

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]

print(friends[1]["name"])


student_attendances = {"Rolf": 96, "Bob": 80, "Anne": 100}

if "Bob" in student_attendances:
    print(student_attendances["Bob"])
else:
    print("No one here has attended the class")
#for student, attendance in student_attendances.items():
 #   print(f"{student}: {attendance}")
