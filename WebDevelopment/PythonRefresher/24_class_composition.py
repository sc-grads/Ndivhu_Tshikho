class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books"
    
shelf = BookShelf(300)
print(shelf)

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"

book = Book("Harry Potter", 500)
book2 = Book("Python 101", 600)
shelf = BookShelf(book, book2)
print(shelf)    
