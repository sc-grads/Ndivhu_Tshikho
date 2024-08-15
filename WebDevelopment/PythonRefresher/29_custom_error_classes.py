class book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count    
        self.pages_read = 0
    
    def __repr__(self):
        return(
            f"<Book{self.name}, read {self.pages_read} pages out of {self.page_count} pages>"
        )
    
    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise ValueError(
                f"You can't read {pages} pages. This book only has {self.page_count} pages."
            )
        self.pages_read += pages
        return self.pages_read