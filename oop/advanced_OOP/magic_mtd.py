class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"The object is: {self.title}"
    
    def __repr__(self):
        return f"The object is: {self.author}"
    
book1 = Book("Hadis", "Bealu")
print(book1)