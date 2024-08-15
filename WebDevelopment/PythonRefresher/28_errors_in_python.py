def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("divisor cannot be 0")
    return dividend / divisor

students = [
    {"name": "Alice", "grades": [100, 90]},
    {"name": "Bob", "grades": [90, 85]},
    {"name": "Charlie", "grades": [95, 95]},
    {"name": "David", "grades": [100, 100]},
    {"name": "Eve", "grades": [100, 100]},
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name}: {average}")

except ZeroDivisionError as e:
    print(e)
    print(f"{name} has no grades")

else:
    print("All students have grades")
finally:
    print("End of program")
    