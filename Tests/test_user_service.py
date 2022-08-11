import pytest
import datetime
import dao.user_dao
from service.user_serivce import UserService
from model.user import User


def mock_ud_check_password(self, usn, pwd):
    return [1, 'Bren', 'tabaxi', 'None', 'neverwinter', False]

def mock_ud_create_user(self, user_obj):
    return "Bren successfully registered."

def mock_ud_get_user(self, usn):
    user = User('Bren', 'tabaxi', 'neverwinter')
    user.set_id(1)
    user.set_fav_genre("TTRPG")
    return user



def test_check_password(mocker):
    mocker.patch('dao.user_dao.UserDao.check_password', mock_ud_check_password)
    us = UserService()
    actual = us.check_password('Bren', 'tabaxi')

    assert actual == {'admin': False, 'username': 'Bren'}


def test_create_user(mocker):
    mocker.patch('dao.user_dao.UserDao.create_user', mock_ud_create_user)
    us = UserService()
    actual = us.create_user(User('Bren', 'tabaxi', 'neverwinter'))

    assert actual == "Bren successfully registered."


def test_get_user_exists(mocker):
    def mock_ud_get_user(self, usn):
        user = User('Bren', 'tabaxi', 'neverwinter')
        user.set_id(1)
        user.set_fav_genre("TTRPG")
        return user

    mocker.patch('dao.user_dao.UserDao.get_user', mock_ud_get_user)

    def mock_ud_get_all_usernames(self):
        return ['Bren', 'Elwy', 'Caerlin']

    mocker.patch('dao.user_dao.UserDao.get_all_usernames', mock_ud_get_all_usernames)
    us = UserService()
    actual = us.get_user('Bren').to_dict()

    assert actual == {'favorite genre': 'TTRPG', 'joined': 'neverwinte', 'reviews': [], 'username': 'Bren'}

def test_get_user_dne(mocker):

    mocker.patch('dao.user_dao.UserDao.get_user', mock_ud_get_user)

    def mock_ud_get_all_usernames(self):
        return ['Bren', 'Elwy', 'Caerlin']

    mocker.patch('dao.user_dao.UserDao.get_all_usernames', mock_ud_get_all_usernames)
    us = UserService()

    with pytest.raises(Exception) as e:
        us.get_user('Marko').to_dict()


def test_get_all_users(mocker):
    def mock_ud_get_all_users(self):
        user1 = User('Bren', 'tabaxi', 'neverwinter')
        user1.set_id(1)
        user1.set_fav_genre("TTRPG")

        user2 = User('Caerlin', 'dragonborn', 'neverwinter')
        user2.set_id(2)
        user2.set_fav_genre("TTRPG")

        user3 = User('Elwy', 'elf', 'neverwinter')
        user3.set_id(3)
        user3.set_fav_genre("TTRPG")

        return [user1.to_dict(), user2.to_dict(), user3.to_dict()]

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_ud_get_all_users)
    us = UserService()
    actual = us.get_all_users()
    assert actual == [{'favorite genre': 'TTRPG', 'joined': 'neverwinte',  'reviews': [], 'username': 'Bren'},
                     {'favorite genre': 'TTRPG','joined': 'neverwinte','reviews': [], 'username': 'Caerlin'},
                     {'favorite genre': 'TTRPG', 'joined': 'neverwinte','reviews': [], 'username': 'Elwy'}]


def test_update_fav_genre(mocker):
    def mock_ud_get_all_usernames(self):
        return ['Bren', 'Elwy', 'Caerlin']

    mocker.patch('dao.user_dao.UserDao.get_all_usernames', mock_ud_get_all_usernames)


    us = UserService()
