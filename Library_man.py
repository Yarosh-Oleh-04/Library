import Library

LIBRARY_ROOT = "Books/books.txt"

def printBooks(books):
    ln = len(books)
    for i in range(ln): print(i + 1, books[i], sep=': ')


def lookForABook(lib):
    print("Enter book name:")
    name = input('=>')

    foundBooks = lib.findBooks(name=name)

    if foundBooks:
        print("Books found:")
        printBooks(foundBooks)
    else:
        print("No match found.")

    return foundBooks


def borrowABook(books):
    print('Choose a book to borrow:')
    num = int(input("=>"))

    book = books[num]
    book.isAvailable = False

    print("Book" + str(book) + " borrowed!")


def Choose(option):
    lib = Library.Library(LIBRARY_ROOT)
    libBooks = lib.getBooks()
    foundBooks = []

    # print all
    if option == '1':
        foundBooks = libBooks.copy()
        printBooks(foundBooks)

    # look for a book
    elif option == '2':
        lookForABook(lib)

    elif option == '3':
        while foundBooks is None or len(foundBooks) <= 0:
            foundBooks = lookForABook(lib)

        borrowABook(foundBooks)

    elif option == '4':
        pass

    elif option == '5':
        pass

    elif option == '6':
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
5. Search by parameters
6. Exit
""")

    opt = input("=>")
    Choose(opt)
