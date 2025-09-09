class Book:

    def __init__(self,idOfBook,title,author,isAvailable = True):
        self.idOfBook = idOfBook
        self.title = title
        self.author = author
        self.isAvailable = isAvailable

    def borrowBook(self):
        if self.isAvailable:
            self.isAvailable = False
            return True
        return False

    def returnBook(self):
        self.isAvailable = True

    def displayInfo(self):
        print(f"The book id is {self.idOfBook} ,Title of the book is {self.title} ,Author of the book is {self.author} ,book availability {self.isAvailable}")


class Member:

    def __init__(self,memeberId,name):
        self.memberId = memeberId
        self.name = name
        self.borrowedBooks = []
        
    def borrow(self,book):
        if book.borrowBook():
            self.borrowedBooks.append(book)
            print(f"{self.name} has borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is not available for now")

    def returnTheBook(self,book):
        if book in self.borrowedBooks:
            book.returnBook()
            self.borrowedBooks.remove(book)
            print(f"{self.name} has returned {book.titel}")
        else:
            print(f"{self.name} does not have {book.title}")

    def displayBorrowedBooks(self):
        if not self.borrowedBooks:
            print(f"{self.name} has not borrowed any books yet")

        else:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowedBooks:
                print(book.title)


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def addBook(self,book):
        self.books.append(book)

    def removeBook(self,book):
        self.books.remove(book)

    def addMember(self,member):
        self.members.append(member)

    def findBook(self,title,author,idOfBook):
        self.title = title
        self.author = author
        self.idOfBook = idOfBook

        for book in self.books:
            if(idOfBook and self.idOfBook == idOfBook)or \
            (title and self.title == title)or \
            (author and self.author == author):
                return book
        return None
    
    def displayInfo(self):
        print(self.idOfBook , self.title , self.author)

    def showAllBooks(self):
        if not self.books:
            print("No books in the library")

        else:
            print("Library books : ")
            for book in self.books:
                book.displayInfo()

lib = Library()

# Adding Books
book1 = Book(1,"Rich dad Poor dad" , "Robert t kiyosaki")
book2 = Book(2,"Think and grow rich" , "Nepolien hill")
book3 = Book(3,"Phychology of money" , "morgen housil")
book4 = Book(4,"intelligent Investor" , "benjamin graham")

lib.addBook(book1)
lib.addBook(book2)
lib.addBook(book3)
lib.addBook(book4)

# Adding Members
member1 = Member(101,"Ketul")
member2 = Member(102,"Kushal")
member3 = Member(103,"Maulik")

lib.addMember(member1)
lib.addMember(member2)
lib.addMember(member3)

# Listing all books
lib.showAllBooks()

# Borrowing books
member1.borrow(book1)
member2.borrow(book2)
member3.borrow(book1)

# Displaying the borrowing books
member1.displayBorrowedBooks()

# Returning the book
member1.returnTheBook("Rich dad poor dad")