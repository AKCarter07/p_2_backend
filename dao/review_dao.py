import psycopg
from model.review import Review
import os

class ReviewDao:
    def __init__(self):
        pass


# Create
    def new_review(self, rev_obj):
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname="", user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO reviews (isbn, review, usr, rating) VALUES "
                            f"(%s, %s, %s, %s);", (rev_obj.isbn, rev_obj.review, rev_obj.user, rev_obj.rating))

# Read
    def get_reviews(self, usn, isbn):
        call = "SELECT * FROM reviews INNER JOIN books ON reviews.isbn = books.isbn"
        if usn:
            call = call + f" where usr = '{usn}'"
        if isbn:
            call = call + f" where isbn = '{isbn}'"
        call = call + ";"
        reviews = []
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname="", user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(call)
                for line in cur:
                    rev = Review(line[0], line[6], line[5], line[2], line[1], line[3])
                    reviews.append(rev)
                return reviews


# Update

# Delete
    def delete_review(self, isbn, user):
        return f"Did you really think you could delete something from the internet, {user}?"





