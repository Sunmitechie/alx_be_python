class Book:
    """A class representing a book with a title, an author, and its availability status."""

    def __init__(self, title, author):
        """
        Initialize a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if self._is_checked_out:
            return False  # Book is already checked out
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as available."""
        if not self._is_checked_out:
            return False  # Book is already available
        self._is_checked_out = False
        return True

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books in a library."""

    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """
        Add a new book to the library.

        Args:
            book (Book): An instance of the Book class.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book from the library by its title.

        Args:
            title (str): The title of the book to check out.

        Returns:
            str: A message indicating the result of the operation.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"'{title}' has been checked out."
                else:
                    return f"Error: '{title}' is already checked out."
        return f"Error: '{title}' not found in the library."

    def return_book(self, title):
        """
        Return a book to the library by its title.

        Args:
            title (str): The title of the book to return.

        Returns:
            str: A message indicating the result of the operation.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"'{title}' has been returned."
                else:
                    return f"Error: '{title}' was not checked out."
        return f"Error: '{title}' not found in the library."

    def list_available_books(self):
        """Print a list of all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
