class Library:
    def __init__(self):
        self.no_books=0
        self.books=[]

    def addBooks(self,book):
        self.books.append(book)
        self.no_books=len(self.books)
    def showinfo(self):
        print(f"The number of books: {self.no_books}")
        for book in (self.books):
            print(book)
l1=Library()
l1.addBooks("120")
l1.addBooks("Harry Potter")
l1.addBooks("Harry Potter")
l1.addBooks("Harry Potter")
l1.showinfo()
