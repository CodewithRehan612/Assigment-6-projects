class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage:
if __name__ == "__main__":
    print(f"Total books: {Book.total_books}")
    Book.increment_book_count()
    print(f"Total books: {Book.total_books}")
    Book.increment_book_count()
    print(f"Total books: {Book.total_books}") 
