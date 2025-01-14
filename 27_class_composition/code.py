# Composition


# eg. this code above is weird

# 1 - A Book is not a BookShelf
# 2 - There's no sense of using inheritance, if you will not inherit aniything (eg. the __str__ overriding)

# class BookShelf:
#     def __init__(self, quantity):
#         self.quantity = quantity

#     def __str__(self):
#         return f"BookShelf with {self.quantity} books."
    

# shelf = BookShelf(300)

# class Book(BookShelf):
#     def __init__(self, name, quantity):
#         super().__init__(quantity)
#         self.name = name

#     def __str__(self):
#         return f"Book {self.name}"

# book = Book("Harry Potter", 120)

# print(book)

# The right way, using composition
# A BookShelf can store many books

class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
    
class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"
    

book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)

print(shelf)