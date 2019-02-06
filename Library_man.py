import Library

LIBRARY_ROOT = "Books/books.txt"


def printBooks(books):
    print('0. Borrow book\n')
    ln = len(books)
    for i in range(ln): print(i + 1, books[i], sep=': ')


def lookForABook(lib):
    print("Enter book name:")
    name = input('=>')

    found_books = lib.findBooks(name=name)

    if found_books:
        print("Books found:")
        printBooks(found_books)
    else:
        print("No match found.")
    return found_books


def borrowABook(books, lib):
    print('Choose a book to borrow:')
    num = int(input("=>")) - 1
    if str(books[num]).split(',')[4] == ' \nAvailable: false ':
        print('This book is not available')
        return 0
    book = str(books[num]).split('\n')[0]
    lib.borrowBook(book)
    print("Book: " + book + "borrowed!")


def Choose(option, found_books):
    lib = Library.Library(LIBRARY_ROOT)
    libBooks = lib.getBooks()

    # print all
    if option == '1':
        found_books = libBooks.copy()
        printBooks(found_books)

    # look for a book
    elif option == '2':
        found_books = lookForABook(lib)

    elif option == '3':
        new_book = []
        new_book += [input('Name => ')]
        new_book += [input('Author => ')]
        new_book += [input('Publisher => ')]
        new_book += [input('Year => ')]
        new_book += ['true']
        new_book += [input('Catalog number => ')]
        lib.addBook(new_book)
        print('Succed!')

    elif option == '0':
        borrowABook(found_books, lib)

    elif option == '4':
        pass

    elif option == '5':
        print("""
Search by:
1. name
2. author
3. publisher
4. year
        """)
        by = input('=>')
        what = input('=>')
        name = what if by == '1' else ''
        author = what if by == '2' else ''
        publisher = what if by == '3' else ''
        year = what if by == '4' else ''
        found_books = lib.findBooks(name=name, author=author, publisher=publisher, year=year)

        if found_books:
            print("Books found:")
            printBooks(found_books)
        else:
            print("No match found.")

    elif option == '6':
        lib.storeBooks()
        print("Thanks for using our services. Good bye!")
        exit()
    else:
        print("No such option available.")
    pass

    return found_books


print("Welcome to the library!")

foundBooks = []

while True:
    print("\nChoose an option:")
    print("""
1. Show all books
2. Look for a book
3. Add book
4. Return a book
5. Search by parameters
6. Exit
""")

    opt = input("=>")

    foundBooks = Choose(opt, foundBooks)
