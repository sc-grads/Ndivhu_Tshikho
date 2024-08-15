class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

student_1 = Student("Mark", 20)
print(student_1.get_age())
print(student_1.get_name())
    

