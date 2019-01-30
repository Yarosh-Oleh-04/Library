import Book
import Library

LIBRARY_ROOT="Books/books.txt"

def Choose(opt):
    lib = Library.Library(LIBRARY_ROOT)
    list = lib.getBooks()
    
    if opt=='1':
        for i in list: print(i)
    elif opt =='2':
        print("Enter book name:")
        name = input('=>')
        if lib.hasBook(Book.Book(name, '', '', '', '', '')):
            print("A book found:")
            
            books = lib.findBooks(name=name)
            
            if(books is not None and books.any()):
               for b in books:
                   b.print()
        else:
            print("No match found.")
        
    elif opt == '3':
        pass
    elif opt == '4':
        pass
    elif opt == '5':
        lib.storeBooks()
        print("Thanks for using our services. Good bye!")
        exit()
    else:
        print("No such option available.")
    pass

print("Welcome to the library!")

while True:
    print("\nChoose an option:")
    print("""
1. Show all books
2. Look for a book
3. Borrow a book
4. Return a book
5. Exit
""")
    
    opt = input("=>")
    Choose(opt)
    
    
    