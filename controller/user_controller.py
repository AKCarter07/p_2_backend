from flask import Blueprint, request, session, current_app
import json
from model.user import User
from service.user_serivce import UserService
from exception.invalid_param_error import InvalParam
import datetime

uc = Blueprint('user_controller', __name__)
us = UserService()


@uc.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and "user" not in session:
        print("user_controller/login :: method = POST")
        json_input = request.get_json()
        usn = json_input['username']
        pwd = json_input['password']
        try:
            key = us.check_password(usn, pwd)
            print("user_controller/login :: key: ", key)
            session["user"] = key
            return session["user"], 200
        except InvalParam as e:
            return{
                "message": f"{e}"
            }, 400
    elif "user" in session:
         return session["user"], 200
    else:
        return "something went wrong"


@uc.route('/logout', methods=['POST'])
def logout():
    [session.pop(key) for key in list(session.keys())]
    print(session)
    return {
        'message': 'logout successful'
    }, 201


# Create
@uc.route('/new-user', methods=['POST'])
def create_user():
    usn = request.form.get('username')
    pwd = request.form.get('password')
    joined = datetime.date.today()
    user = User(usn, pwd, joined)
    try:
        return us.create_user(user)
    except InvalParam as e:
        return {
                   "message": f"{e}"
               }, 400


# Read
@uc.route('/users/<usn>')
def get_user(usn):
    try:
        return us.get_user(usn).to_dict()
    except InvalParam as e:
        return {
                   "message": f"{e}"
               }, 400


@uc.route('/users')
def get_all_users():
    users = []
    for user in us.get_all_users():
        users.append(user.to_dict())
    return json.dumps(users)


# Update
@uc.route('/users/<usn>', methods = ['PUT'])
def update_fav_genre(usn):
    if "user" in session:
        fav_genre = request.form.get('fav-genre')
        return us.update_fav_genre(usn, fav_genre)
    else:
        return "Not logged in"


@uc.route('/admin/<usn>', methods = ['PUT'])
def update_admin(usn):
    if "user" in session:
        if session['user']['admin']:
            admin = request.form.get('is-admin')
            return us.update_admin(usn, admin)
        else:
            return "Must be an admin to change admin privileges."
    else:
        return "Not logged in"


# Delete
@uc.route('/users/<usn>',  methods = ['DELETE'])
def delete_user(usn):
    return us.delete_user(usn)
