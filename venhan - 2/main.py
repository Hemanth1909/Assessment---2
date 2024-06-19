class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn= isbn
        self.genre = genre
        self.quantity = quantity

    def displayinfo(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nGenre: {self.genre}\nAvailable: {self.quantity}\n")



class Library:
    def __init__(self):
        self.books = []
        self.borrow_list = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_books(self):
        print("List of Library Books:")
        for book in self.books:
            book.displayinfo()
    
    def book_search(self, book_title):
        for book in self.books:
            if(book.title == book_title):
                print(f"Book {book_title} is available in the Libreary")
                break
        
        print(f"Book {book_title} is not available in the Libreary")

    def borrow_book(self, book_title, member_id):
        for book in self.books:
            if book.title == book_title and book.quantity >= 1:
                book.quantity -= 1
                print(f"Book {book_title} has been borrowed.")
                self.borrow_list[member_id] = {"title": book_title, "ISBN": book.isbn}
                return
        print(f"Sorry, '{book_title}' is either not available or does not exist in the library.")


    def return_book(self, book_title, member_id):
        for book in self.books:
            if book.title == book_title and member_id in self.borrow_list:
                book.quantity += 1
                del self.borrow_list[member_id]
                print(f"Book {book_title} has been returned.")
                return


b1 = Book("Jane Austen", "Pride and Prejudice", "ISB0001","fantasy", 5)
b2 = Book("Great Expectations", "Charles Dickens", "ISB0002", "drama", 8)
b3 = Book("The Adventures of Huckleberry Finn", "Mark Twain", "ISB0003", "cinema", 4)
b4 = Book("To the Lighthouse", "Virginia Woolf", "ISB0004", "drama", 9)
b5 = Book("War and Peace", "Leo Tolstoy", "ISB0005", "thriller", 6)

lib = Library()
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
lib.add_book(b4)
lib.add_book(b5)

print("Books in the Libreary")
lib.display_books()

lib.borrow_book("Jane Austen", "ID001")
print("Books after Borrowing")
lib.display_books()
print("Borrow list after borrowing")
print(lib.borrow_list)

lib.return_book("Jane Austen", "ID001")
print("Books after returning")
lib.display_books()
print("Borrow list after returning the book")
print(lib.borrow_list)