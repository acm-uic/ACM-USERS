# groups/controllers.py
# Written by Jeff Kaleshi

from flask import Blueprint, jsonify

from app import ldap
from .util import create_users_dictionary
from .models import ID, EMAIL, NAME, USERNAME

users = Blueprint('users', __name__)

@users.route('/')
def get_all_users():
    '''
        Endpoint to get all users
        :return: Json list of users
    '''
    response = {'errors': [], 'users': []}
    users = ldap.users.search_users()
    
    if users != None:
        response['users'] = create_users_dictionary(users)
    else:
        response['errors'].append('Could not connect to LDAP Server')

    return jsonify(response)

@users.route('/id/<id>')
def get_user_by_id(id):
    '''
        Endpoint to get a single user by id
        :id: string
        :return: Json of a single user
    '''
    response = {'errors': [], 'user': None}
    users = ldap.users.search_users(id, ID)

    if users != None:
        if users:
            response['user'] = users[0].get_json()
    else:
        response['errors'].append('Could not connect to LDAP Server')

    return jsonify(response)

@users.route('/username/<username>')
def get_user_by_username(username):
    '''
        Endpoint to get list of users by username
        :username: string
        :return: Json list of users
    '''
    response = {'errors': [], 'users': []}
    users = ldap.users.search_users(username, USERNAME)

    if users != None:
        response['users'] = create_users_dictionary(users)
    else:
        response['errors'].append('Could not connect to LDAP Server')

    return jsonify(response)

@users.route('/name/<name>')
def get_user_by_name(name):
    '''
        Endpoint to get list of users by name
        :name: string
        :return: Json list of users
    '''
    response = {'errors': [], 'users': []}
    users = ldap.users.search_users(name, NAME)

    if users != None:
        response['users'] = create_users_dictionary(users)
    else:
        response['errors'].append('Could not connect to LDAP Server')

    return jsonify(response)

@users.route('/email/<email>')
def get_user_by_email(email):
    '''
        Endpoint to get list of users by email
        :email: string
        :return: Json list of users
    '''
    response = {'errors': [], 'users': []}
    users = ldap.users.search_users(email, EMAIL)

    if users != None:
        response['users'] = create_users_dictionary(users)
    else:
        response['errors'].append('Could not connect to LDAP Server')

    return jsonify(response)