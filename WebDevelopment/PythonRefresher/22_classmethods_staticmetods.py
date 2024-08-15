class ClassTest:
    def instance_method(self):
        print(f"called instance_method : {self}")

    @classmethod
    def class_method(cls):
        print(f"called class_method : {cls}")

    @staticmethod    
    def static_method():
        print("called static_method")

ClassTest.class_method()



#######################################################
class Book:
    Types = ("Hardcover", "Paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight    

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.Types[0], weight+100)

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.Types[1], weight)


book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)
print(book)
print(light)