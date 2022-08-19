import psycopg
from dao.review_dao import ReviewDao
from model.book import Book
import os

class BookDao:
    def __init__(self):
        self.rd = ReviewDao()

    def get_all_isbns(self):
        isbns = []
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT isbn FROM books")
                for line in cur:
                    isbns.append(line[0])
                return isbns

# Create
    def new_book(self, book_obj):
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO books (isbn, title, author, edition, genre, media_type) VALUES "
                            f"(%s, %s, %s, %s, %s, %s);", (book_obj.isbn, book_obj.title, book_obj.author, book_obj.edition,
                                                       book_obj.genre, book_obj.type))
                conn.commit()


# Read
    def get_book(self, isbn):
        book = None
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM books WHERE isbn = '{isbn}';")
                for line in cur:
                    book = Book(line[0], line[1], line[2], line[3], line[4], line[5])
                revs = self.rd.get_reviews(None, isbn)
                for rev in revs:
                    book.set_review(rev)
                return book

    def get_books_by_title(self, title):
        t = title.split()
        books = []
        call = f"SELECT * FROM books WHERE"
        for _ in t:
            call = call + f" title LIKE '%{_}%' OR"
        call = call[:-3];
        call = call + ";"
        print(call)
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(call)
                for line in cur:
                    book = Book(line[0], line[1], line[2], line[3], line[4], line[5])
                    revs = self.rd.get_reviews(None, book.isbn)
                    books.append(book)
                    for rev in revs:
                        book.set_review(rev)
                return books

    def get_genre_list(self):
        genres = []
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT DISTINCT genre FROM books")
                for line in cur:
                    genres.append(line)
                return genres

# Update
    def edit_book_attributes(self, book_obj):
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE books SET title = '{book_obj.title}', author = '{book_obj.author}',"
                            f"edition = '{book_obj.edition}', genre = '{book_obj.genre}' "
                            f"WHERE isbn = '{book_obj.isbn}';")
                conn.commit()


    def edit_isbn(self, old_isbn, new_book_obj):
        self.new_book(new_book_obj)
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE reviews SET isbn = '{new_book_obj.isbn}' WHERE isbn = '{old_isbn}';")
                cur.execute(f"DELETE FROM books WHERE isbn = '{old_isbn}';")
                conn.commit()


# Delete
    def delete_book(self, isbn):
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM books WHERE isbn = '{isbn}';")
                conn.commit()
