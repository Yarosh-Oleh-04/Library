import Book
import Library

LIBRARY_ROOT="Books/books.txt"

def Choose(opt):
    lib = Library.Library(LIBRARY_ROOT)
    
    if opt=='1':
        list = "\n".join([str(lib.getBooks()[0])])
        print(list)
        pass
    elif opt =='2':
        print("Enter book name:")
        name = input('=>')
        book = name.split(',')
        if lib.hasBook(Book(book[0], book[1], '', 0, True, 111)):
            print("A book found:")
            
            books = lib.findBooks(name=book[0], author=book[1])
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

while True:
    print("Welcome to the library!/n Choose an option:")
    print("""
1. Show all books
2. Look for a book
3. Borrow a book
4. Return a book
5. Exit
""")
    
    opt = input("=>")
    Choose(opt)
    
    
    