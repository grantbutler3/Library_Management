# Base class for a Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"Book '{self.title}' borrowed successfully."
        else:
            return f"Book '{self.title}' is already borrowed."

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"Book '{self.title}' returned successfully."
        else:
            return f"Book '{self.title}' was not borrowed."

# Class for managing the Library system
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def list_books(self):
        if self.books:
            print("\nBooks in the library:")
            for book in self.books:
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"{book} - {status}")
        else:
            print("No books in the library.")

    def borrow_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            print(book.borrow())
        else:
            print(f"No book found with ISBN {isbn}.")

    def return_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            print(book.return_book())
        else:
            print(f"No book found with ISBN {isbn}.")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

# Child class for managing E-Books (a subclass of Book)
class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - Format: {self.file_format}"

# Child class for managing Physical Books (a subclass of Book)
class PhysicalBook(Book):
    def __init__(self, title, author, isbn, weight):
        super().__init__(title, author, isbn)
        self.weight = weight

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - Weight: {self.weight}kg"

# Demo of the Library Management System
def demo():
    library = Library()

    # Create some books
    book1 = PhysicalBook("1984", "George Orwell", "1234567890", 0.5)
    book2 = EBook("Python Programming", "John Doe", "9876543210", "PDF")
    book3 = PhysicalBook("The Catcher in the Rye", "J.D. Salinger", "1122334455", 0.3)

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # List available books
    library.list_books()

    # Borrow some books
    library.borrow_book("1234567890")
    library.borrow_book("9876543210")

    # List available books again
    library.list_books()

    # Return a book
    library.return_book("1234567890")

    # List available books after returning
    library.list_books()

# Run the demo
if __name__ == "__main__":
    demo()
