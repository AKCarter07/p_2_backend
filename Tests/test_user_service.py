import pytest
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

def mock_ud_get_all_usernames(self):
    return ['Bren', 'Elwy', 'Caerlin']

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

def mock_ud_update_fav_genre(self, usn, fav_genere):
    return None

def mock_ud_update_admin(self, usn, admin):
    return None

def mock_ud_delete_user(self, usn):
    return None


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
    mocker.patch('dao.user_dao.UserDao.get_user', mock_ud_get_user)
    mocker.patch('dao.user_dao.UserDao.get_all_usernames', mock_ud_get_all_usernames)
    us = UserService()
    actual = us.get_user('Bren').to_dict()

    assert actual == {'favorite genre': 'TTRPG', 'joined': 'neverwinte', 'reviews': [], 'username': 'Bren'}

def test_get_user_dne(mocker):

    mocker.patch('dao.user_dao.UserDao.get_user', mock_ud_get_user)
    mocker.patch('dao.user_dao.UserDao.get_all_usernames', mock_ud_get_all_usernames)
    us = UserService()

    with pytest.raises(Exception) as e:
        us.get_user('Marko').to_dict()


def test_get_all_users(mocker):

    mocker.patch('dao.user_dao.UserDao.get_all_users', mock_ud_get_all_users)
    us = UserService()
    actual = us.get_all_users()
    assert actual == [{'favorite genre': 'TTRPG', 'joined': 'neverwinte',  'reviews': [], 'username': 'Bren'},
                     {'favorite genre': 'TTRPG','joined': 'neverwinte','reviews': [], 'username': 'Caerlin'},
                     {'favorite genre': 'TTRPG', 'joined': 'neverwinte','reviews': [], 'username': 'Elwy'}]


def test_update_fav_genre_pos(mocker):
    mocker.patch('dao.user_dao.UserDao.get_all_usernames', mock_ud_get_all_usernames)
    mocker.patch('dao.user_dao.UserDao.update_fav_genre', mock_ud_update_fav_genre)
    us = UserService()
    actual = us.update_fav_genre('Bren', 'fantasy')
    assert actual == None

def test_update_fav_genre_neg(mocker):
    mocker.patch('dao.user_dao.UserDao.get_all_usernames', mock_ud_get_all_usernames)
    mocker.patch('dao.user_dao.UserDao.update_fav_genre', mock_ud_update_fav_genre)
    us = UserService()
    with pytest.raises(Exception) as e:
        us.update_fav_genre('Marko', 'music')

def test_update_admin_pos(mocker):
    mocker.patch('dao.user_dao.UserDao.get_all_usernames', mock_ud_get_all_usernames)
    mocker.patch('dao.user_dao.UserDao.update_admin', mock_ud_update_admin)
    us = UserService()
    actual = us.update_admin('Bren', True)
    assert actual == None

def test_update_admin_neg(mocker):
    mocker.patch('dao.user_dao.UserDao.get_all_usernames', mock_ud_get_all_usernames)
    mocker.patch('dao.user_dao.UserDao.update_admin', mock_ud_update_admin)
    us = UserService()
    with pytest.raises(Exception) as e:
        us.update_admin('Marko', True)


def test_delete_user(mocker):
    mocker.patch('dao.user_dao.UserDao.get_all_usernames', mock_ud_get_all_usernames)
    mocker.patch('dao.user_dao.UserDao.delete_user', mock_ud_delete_user)
    us = UserService()
    actual = us.delete_user('Bren')
    assert actual == None

def test_update_fav_genre_neg(mocker):
    mocker.patch('dao.user_dao.UserDao.get_all_usernames', mock_ud_get_all_usernames)
    mocker.patch('dao.user_dao.UserDao.delete_user', mock_ud_delete_user)
    us = UserService()
    with pytest.raises(Exception) as e:
        us.delete_user('Marko')