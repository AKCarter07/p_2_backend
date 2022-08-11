import pytest
from service.book_service import BookService
from model.book import Book

def mock_bd_get_all_isbns(self):
    return [123, 223, 323]


def mock_bd_new_book(self, book_obj):
    return None


def mock_bd_get_book(self, isbn):
    book = Book(123, "Title", "Author McAuthor", 1, "genre", "book")
    return book


def mock_bd_get_genre_list(self):
    return ["fiction", "fantasy", "TTRPG", "genre"]


def mock_bd_edit_book_attributes(self, book_obj):
    return None


def mock_bd_edit_isbn(self, old_isbn, new_book_obj):
    return None


def mock_bd_delete_book(self, isbn):
    return None


def test_new_book_pos(mocker):
    mocker.patch('dao.book_dao.BookDao.get_all_isbns', mock_bd_get_all_isbns)
    mocker.patch('dao.book_dao.BookDao.new_book', mock_bd_new_book)
    book = Book(423, "Title4", "Author McAuthor", 1, "genre", "book")
    bs = BookService()

    actual = bs.new_book(book)
    assert actual is None

def test_new_book_neg(mocker):
    mocker.patch('dao.book_dao.BookDao.get_all_isbns', mock_bd_get_all_isbns)
    mocker.patch('dao.book_dao.BookDao.new_book', mock_bd_new_book)
    book = Book(123, "Title4", "Author McAuthor", 1, "genre", "book")
    bs = BookService()

    with pytest.raises(Exception) as e:
        bs.new_book(book)


def test_get_book_pos(mocker):
    mocker.patch('dao.book_dao.BookDao.get_all_isbns', mock_bd_get_all_isbns)
    mocker.patch('dao.book_dao.BookDao.get_book', mock_bd_get_book)
    bs = BookService()
    actual = bs.get_book(123).to_dict()
    assert actual == {'author': 'Author McAuthor','edition': 1,'genre': 'genre', 'isbn': 123, 'reviews': [], 'title': 'Title'}


def test_get_book_neg(mocker):
    mocker.patch('dao.book_dao.BookDao.get_all_isbns', mock_bd_get_all_isbns)
    mocker.patch('dao.book_dao.BookDao.get_book', mock_bd_get_book)
    bs = BookService()
    with pytest.raises(Exception) as e:
        bs.get_book(423)


def test_edit_book_attributes_pos(mocker):
    mocker.patch('dao.book_dao.BookDao.get_all_isbns', mock_bd_get_all_isbns)
    mocker.patch('dao.book_dao.BookDao.edit_book_attributes', mock_bd_edit_book_attributes)
    bs = BookService()
    book = Book(123, "Title4", "Author McAuthor", 1, "genre", "book")
    actual = bs.edit_book_attributes(book)
    assert actual is None

def test_edit_book_attributes_neg(mocker):
    mocker.patch('dao.book_dao.BookDao.get_all_isbns', mock_bd_get_all_isbns)
    mocker.patch('dao.book_dao.BookDao.edit_book_attributes', mock_bd_edit_book_attributes)
    bs = BookService()
    book = Book(423, "Title4", "Author McAuthor", 1, "genre", "book")
    with pytest.raises(Exception) as e:
        bs.edit_book_attributes(book)


def test_edit_isbn_pos(mocker):
    mocker.patch('dao.book_dao.BookDao.get_all_isbns', mock_bd_get_all_isbns)
    mocker.patch('dao.book_dao.BookDao.edit_isbn', mock_bd_edit_isbn)
    bs = BookService()
    book = Book(423, "Title4", "Author McAuthor", 1, "genre", "book")
    actual = bs.edit_isbn(123, book)
    assert actual is None


def test_edit_isbn_neg(mocker):
    mocker.patch('dao.book_dao.BookDao.get_all_isbns', mock_bd_get_all_isbns)
    mocker.patch('dao.book_dao.BookDao.edit_isbn', mock_bd_edit_isbn)
    bs = BookService()
    book = Book(123, "Title4", "Author McAuthor", 1, "genre", "book")
    with pytest.raises(Exception) as e:
        bs.edit_isbn(423, book)


def test_delete_book():
    bs = BookService()
    actual = bs.delete_book('123')
    assert actual == "Technically, the ability to delete books has been programmed in, but no, no you may not. " \
               "Please submit in writing to the management team why you think a book should be deleted from our database." \
               "Be prepared to recieve a long lecture referencing the Library of Alexandria." \
               "The answer will still be no."

    # mocker.patch('dao.book_dao.BookDao.')
    # bs = BookService()
