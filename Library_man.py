import Book
import Library

LIBRARY_ROOT="/Books"

def Choose(opt):
    lib = Library.Library()
    
    if opt=='1':
        pass
    elif opt =='2':
        pass
    elif opt == '3':
        pass
    elif opt == '4':
        pass
    elif opt == '5':
        lib.storeBooks()
        print("Thanks for using our services. Good bye!")
        exit()
    pass

while True:
    print("Welcome to the library!/n Choose an option:")
    print("""
1. See all books
2. Look for a book
3. Borrow a book
4. Return a book
5. Exit
""")
    
    opt = input("=>")
    Choose(opt)
    
    
    