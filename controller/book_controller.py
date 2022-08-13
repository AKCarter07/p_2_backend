from flask import Blueprint, request, session, current_app
import json
from service.book_service import BookService
from model.book import Book
from exception.invalid_param_error import InvalParam

bc = Blueprint('book_controller', __name__)
bs = BookService()


# Create
@bc.route('/book', methods=['POST'])
def new_book():
    isbn = request.form.get('isbn')
    title = request.form.get('title')
    author = request.form.get('author')
    edition = request.form.get('edition')
    genre = request.form.get('genre')
    type = request.form.get('type')
    book = Book(isbn, title, author, edition, genre, type)
    try:
        bs.new_book(book)
        return {
            "message": f"{title} added to database"
        }, 201
    except InvalParam as e:
        return {
                   "message": f"{e}"
               }, 400


# Read
@bc.route('/books/<isbn>')
def get_book(isbn):
    try:
        return bs.get_book(isbn).to_dict()
    except InvalParam as e:
        return {
                   "message": f"{e}"
               }, 400


# Update
@bc.route('/books/<isbn>', methods=['PUT'])
def edit_book_attributes(isbn):
    title = request.form.get('title')
    author = request.form.get('author')
    edition = request.form.get('edition')
    genre = request.form.get('genre')
    type = request.form.get('type')
    book = Book(isbn, title, author, edition, genre, type)
    try:
        bs.edit_book_attributes(book)
        return f"{title} edited."
    except InvalParam as e:
        return {
                   "message": f"{e}"
               }, 400


@bc.route('/books/<oldisbn>', methods=['PUT'])
def edit_isbn(oldisbn):
    new_isbn = request.form.get('new-isbn')
    book = bs.get_book(oldisbn)
    book.isbn = new_isbn
    try:
        bs.edit_isbn(oldisbn, book)
        return f"isbn for {book.title} edited."
    except InvalParam as e:
        return {
                   "message": f"{e}"
               }, 400


# Delete
@bc.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    return "No"
