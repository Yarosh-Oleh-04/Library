import Book

class Library:
    
    def __init__ (self, root):
        self.root = root
        self.books = []
    
    def getBooks(self):
        books = open(self.root, 'r').readlines()
        for i in books:
            elem = i.split(',')
            self.books += [Book.Book(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5])]
        return self.books
    
    def storeBooks(self):
        pass
    
    def addBook(self, book):
        pass
    
    def hasBook(self, book):
        for i in self.books:
            if i.name == book.name and i.author == book.author:
                return True
        return False
    
    def borrowBook(self, book):
        pass
    
    def findBooks(self, author='', name='', publisher='', year='', cat_num='', is_available=''):
        pass
    
LIBRARY_ROOT="Books/books.txt"
lib = Library(LIBRARY_ROOT)
lib.getBooks()
print(str(lib.hasBook(Book.Book('Цифрова фортеця','Ден Браун','','','',''))))