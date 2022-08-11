from dao.book_dao import BookDao
from exception.invalid_param_error import InvalParam

class BookService:
    def __init__(self):
        self.bd = BookDao()

# Create
    def new_book(self, book_obj):
        if book_obj.isbn in self.bd.get_all_isbns():
            raise InvalParam(f"Isbn {book_obj.isbn} already exists in system.")
        else:
            return self.bd.new_book(book_obj)

# Read
    def get_book(self, isbn):
        if isbn in self.bd.get_all_isbns():
            return self.bd.get_book(isbn)
        else:
            raise InvalParam(f"Isbn not in library. Please add book to reveiw.")

# Update
    def edit_book_attributes(self, book_obj):
        if book_obj.isbn in self.bd.get_all_isbns():
            return self.bd.edit_book_attributes(book_obj)
        else:
            raise InvalParam(f"Isbn not in library. Please add book.")

    def edit_isbn(self, old_isbn, new_book_obj):
        if old_isbn in self.bd.get_all_isbns():
            return self.bd.edit_isbn(old_isbn, new_book_obj)
        else:
            raise InvalParam(f"Isbn not in library. Please add book.")

# Delete
    def delete_book(self, isbn):
        return "Technically, the ability to delete books has been programmed in, but no, no you may not. " \
               "Please submit in writing to the management team why you think a book should be deleted from our database." \
               "Be prepared to recieve a long lecture referencing the Library of Alexandria." \
               "The answer will still be no."

