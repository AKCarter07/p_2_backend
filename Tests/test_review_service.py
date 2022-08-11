import pytest
from service.review_service import  ReviewService
from model.review import Review

def mock_rd_new_review(self, rev_obj):
    return None

def mock_rd_get_reviews(self, usn, isbn):
    review = Review(123," Author McAuthorstein", "Title", "User", "This is an review. Such a pretty review.", 5)
    if usn == "User" or isbn == 123:
        return review


def mock_rd_delete_review(self, isbn, user):
    return f"Did you really think you could delete something from the internet, {user}?"


def test_new_review(mocker):
    mocker.patch('dao.review_dao.ReviewDao.new_review', mock_rd_new_review)
    rs = ReviewService()
    review = Review(123," Author McAuthorstein", "Title", "User", "This is an review. Such a pretty review.", 5)
    assert rs.new_review(review) is None

def test_get_reviews_by_usn(mocker):
    mocker.patch('dao.review_dao.ReviewDao.get_reviews', mock_rd_get_reviews)
    rs = ReviewService()
    actual = rs.get_reviews("User", None).to_dict()
    assert actual == {'author': ' Author McAuthorstein', 'isbn': 123, 'rating': 5,
                      'review': 'This is an review. Such a pretty review.', 'reviewer': 'User', 'title': 'Title'}


def test_get_reviews_by_isbn(mocker):
    mocker.patch('dao.review_dao.ReviewDao.get_reviews', mock_rd_get_reviews)
    rs = ReviewService()
    actual = rs.get_reviews(None, 123).to_dict()
    assert actual == {'author': ' Author McAuthorstein', 'isbn': 123, 'rating': 5,
                      'review': 'This is an review. Such a pretty review.', 'reviewer': 'User', 'title': 'Title'}



def test_delete_review(mocker):
    mocker.patch('dao.review_dao.ReviewDao.delete_review', mock_rd_delete_review)
    rs = ReviewService()
    assert rs.delete_review(123, "User") == "Did you really think you could delete something from the internet, User?"