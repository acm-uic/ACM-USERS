# groups/controllers.py
# Written by Jeff Kaleshi

from flask import Blueprint, jsonify

from app import ldap
from app.users.util import create_users_dictionary
from app.users.models import ACM_MEMBERS, ACM_NOT_PAID, ACM_OFFICERS, ACM_PAID

groups = Blueprint('groups', __name__)

@groups.route('/paid')
def paid_users():
    '''
        Endpoint to get all paid users
        :return: Json list of users
    '''
    response = {'errors': [], 'users': []}
    users = ldap.groups.get_group_members(ACM_PAID)
    
    if users != None:
       response['users'] = create_users_dictionary(users)
    else:
        response['errors'].append('Could not connect to LDAP Server')
    
    return jsonify(response)

@groups.route('/unpaid')
def unpaid_users():
    '''
        Endpoint to get all unpaid users
        :return: Json list of users
    '''
    response = {'errors': [], 'users': []}
    users = ldap.groups.get_group_members(ACM_NOT_PAID)

    if users != None:
        response['users'] = create_users_dictionary(users)
    else:
        response['errors'].append('Could not connect to LDAP Server')

    return jsonify(response)

@groups.route('/members')
def members():
    '''
        Endpoint to get all members
        :return: Json list of users
    '''
    response = {'errors': [], 'users': []}
    users = ldap.groups.get_group_members(ACM_MEMBERS)

    if users != None:
        response['users'] = create_users_dictionary(users)
    else:
        response['errors'].append('Could not connect to LDAP Server')

    return jsonify(response)

@groups.route('/officers')
def officers():
    '''
        Endpoint to get all officers
        :return: Json list of users
    '''
    response = {'errors': [], 'users': []}
    users = ldap.groups.get_group_members(ACM_OFFICERS)

    if users != None:
        response['users'] = create_users_dictionary(users)
    else:
        response['errors'].append('Could not connect to LDAP Server')

    return jsonify(response)
