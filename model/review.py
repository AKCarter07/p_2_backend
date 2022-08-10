class Review:
    def __init__(self, isbn, author, title, user, review, rating):
        self.isbn = isbn
        self.user = user
        self.author = author
        self.title = title
        self.review = review
        self.rating = rating

    def set_auth_title(self, author, title):
        self.author = author
        self.title = title

    def to_dict(self):
        return {
            'isbn': self.isbn,
            'author': self.author,
            'title': self.title,
            'reviewer': self.user,
            'rating': self.rating,
            'review': self.review
        }