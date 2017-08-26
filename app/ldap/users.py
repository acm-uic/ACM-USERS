# ldap/users.py
# Written by Jeff Kaleshi

from ldap3 import Connection, SUBTREE, core

from app.users.models import User
from .util import get_permissions, get_paid_status, generate_user_data

class Users():
    '''
        Manages ldap users
    '''
    def __init__(self, config):
        self._config = config

    def create_user(self):
        '''
            Creates an user in ldap
        '''
        pass

    def search_users(self, field=None, field_type=None):
        '''
            Retrieves all user from ldap and store it in a User object
            :return: [User, User, ...]
        '''
        connection = Connection(
            self._config.server_pool,
            user=self._config.username,
            password=self._config.password
            )

        try:
            connection.bind()
        except core.exceptions.LDAPSocketOpenError:
            return None

        filter = '(objectClass=person)'
        if field and field_type:
            filter ='(&(objectClass=person)({}={}))'.format(field_type, field)

        connection.search(
            search_base='ou=ACMUsers,dc=acm,dc=cs',
            search_filter=filter,
            search_scope=SUBTREE,
            attributes=[
                'displayName', 'name', 'mail', 'memberOf', 
                'sAMAccountName', 'uidNumber'
                ]
            )
        
        users = []
        if connection.entries:

            for query in connection.entries:
                user_data = generate_user_data(query)
                user = User(**user_data)
                users.append(user)

        connection.unbind()
        return users

    def update_user(self):
        '''
            Updates a user in ldap
        '''
        pass

    def delete_user(self):
        '''
            Deletes a user from ldap
        '''
        pass
