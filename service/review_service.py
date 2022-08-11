from dao.review_dao import ReviewDao

class ReviewService():
    def __init__(self):
        self.rd = ReviewDao()

# Create
    def new_review(self, rev_obj):
        return self.rd.new_review(rev_obj)

# Read
    def get_reviews(self, usn, isbn):
        return self.rd.get_reviews(usn, isbn)


# Update

# Delete
    def delete_review(self, isbn, user):
        return self.rd.delete_review(isbn, user)



