class Publisher:
    def __init__(self,name):
        self.name = name

class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title = title
        self.author = author
    def display(self):
        print(f"Title:{self.title}, Author:{self.author},publisher:{self.name}")
class Python(Book):
    def __init__(self,name,title,author,price,pages):
        super().__init__(name,title,author)
        self.price = price
        self.pages = pages
    def display(self):
        super().display()
        print(f"Price:{self.price}")
        print(f"Pages:{self.pages}")
book=Python("Wiley","Introduction to python","john downey",650,320)
book.display()