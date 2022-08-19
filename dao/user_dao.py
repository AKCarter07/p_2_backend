import psycopg
from model.user import User
import os


from dao.review_dao import ReviewDao


class UserDao:
    def __init__(self):
        self.rd = ReviewDao()


    def get_all_usernames(self):
        users = []
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT username FROM users")
                for line in cur:
                    users.append(line[0])
                return users

    def check_password(self, username, password):
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM users WHERE username = '{username}' "
                            f"AND password = '{password}';")
                return cur.fetchone()



# Create
    def create_user(self, user_obj):
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO users (username, password, fav_genre, date_joined) "
                            f"VALUES ('{user_obj.usn}', '{user_obj.pwd}', "
                            f"'{user_obj.fav_genre}', '{user_obj.joined}');")
                conn.commit()
                return f"{user_obj.usn} successfully registered."

# Read
    def get_user(self, usn):
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM users WHERE username = %s", (usn,))
                for line in cur:
                    user = User(line[1], line[2], line[4])
                    user.set_id(line[0])
                    user.set_fav_genre(line[3])
                    user.set_admin(line[5])
                    revs = self.rd.get_reviews(user.usn, None)
                    for rev in revs:
                        user.set_review(rev)
                    return user


    def get_all_users(self):
        users = []
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM users;")
                for line in cur:
                    user = User(line[1], line[2], line[4])
                    user.set_id(line[0])
                    user.set_fav_genre(line[3])
                    user.set_admin(line[5])
                    revs = self.rd.get_reviews(user.usn, None)
                    for rev in revs:
                        user.set_review(rev)
                    users.append(user)
                return users


# Update
    def update_fav_genre(self, usn, fav_genre):
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE users SET fav_genre = '{fav_genre}' WHERE username = '{usn}';")
                conn.commit()

    def update_admin(self, usn, admin):
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE users SET is_admin = '{admin}' WHERE username = '{usn}';")
                conn.commit()

# Delete

    def delete_user(self, usn):
        with psycopg.connect(host=os.environ['P2HOST'], port=os.environ['P2PORT'], dbname=os.environ['P2DB'], user=os.environ['P2USER'],
                             password=os.environ['P2PW']) as conn:
            with conn.cursor() as cur:
                cur.execute(f"DELETE FROM users WHERE username = '{usn}';")
                conn.commit()
