from dao.user_dao import UserDao
from exception.invalid_param_error import InvalParam

class UserService():
    def __init__(self):
        self.ud = UserDao()

    def check_password(self, username, password):
        if username in self.ud.get_all_usernames():
            check = self.ud.check_password(username, password)
            print("user_service, check: ", check)
            if check:
                return {'username': check[1], 'admin': check[5]}
            else:
                raise InvalParam("Password incorrect")
        else:
            raise InvalParam("Username not in database.")


# Create
    def create_user(self, user_obj):
        return self.ud.create_user(user_obj)

# Read
    def get_user(self, usn):
        if usn in self.ud.get_all_usernames():
            return self.ud.get_user(usn)
        else:
            raise InvalParam("Username not in database.")


    def get_all_users(self):
        return self.ud.get_all_users()

# Update
    def update_fav_genre(self, usn, fav_genre):
        if usn in self.ud.get_all_usernames():
            return self.ud.update_fav_genre(usn, fav_genre)
        else:
            raise InvalParam("Username not in database.")


    def update_admin(self, usn, admin):
        if usn in self.ud.get_all_usernames():
            return self.ud.update_admin(usn, admin)
        else:
            raise InvalParam("Username not in database.")

# Delete
    def delete_user(self, usn):
        if usn in self.ud.get_all_usernames():
            return self.ud.delete_user(usn)
        else:
            raise InvalParam("Username not in database.")


