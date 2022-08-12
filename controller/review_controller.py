from flask import Blueprint, request, session, current_app
import json
from service.review_service import ReviewService
from model.review import Review
from exception.invalid_param_error import InvalParam

rc = Blueprint('review_controller', __name__)
rs = ReviewService()


# Create
@rc.route('/book/review', methods=['POST'])
def new_review():
    # if "user" in session:
    isbn = request.form.get('isbn')
    user = request.form.get('user')
    review = request.form.get('review')
    rating = request.form.get('rating')
    author = request.form.get('author')
    title = request.form.get('title')
    rev = Review(isbn, author, title, user, review, rating)
    try:
        return rs.new_review(rev)
    except InvalParam as e:
        return {
                   "message": f"{e}"
               }, 400


# Read

@rc.route("/book/<isbn>/reviews")
def get_all_reviews_for_book(isbn):
    # args = request.args
    # status = args.get('status')
    return {"review": rs.get_all_reviews_for_book(isbn)}


# Update


# Delete
@rc.route('/book/<review>')
def delete_review():
    pass


