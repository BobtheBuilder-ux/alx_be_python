class Book:
    """Class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out
    
    def __str__(self):
        """Return string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Class representing a library that manages books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by its title.
        Returns True if successful, False otherwise.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False
    
    def return_book(self, title):
        """
        Return a book by its title.
        Returns True if successful, False otherwise.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False
    
    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(book)