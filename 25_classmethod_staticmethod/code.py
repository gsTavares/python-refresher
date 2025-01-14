class ClassTest:
    def instance_method(self): # to modify or handle data of the object instance
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls): # used for factory creation
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method(): # you have a reason to put this method here
        print("Called static method.")


test = ClassTest()

test.instance_method()

ClassTest.class_method()

ClassTest.static_method()

# Factory example with @classmethod

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, {self.weight}>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)
        
# Here I can pass an invalid book type
# book = Book("Harry Potter", "abcde", 1500)

# Preventing invalid book types with factories
book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)

print(book)