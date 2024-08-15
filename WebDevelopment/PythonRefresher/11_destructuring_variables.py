x, y = 5, 11

print(x,y)

student_attendance = {"Rolf": 96, "Adam": 100}

print(list(student_attendance.items()))

#for student, attendance in student_attendance.items():
 #   print(f"{student} : {attendance}")


people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f'{name} is {age} years old and works as a {profession}')



head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail) 
