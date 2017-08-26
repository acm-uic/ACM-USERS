# ldap/groups.py
# Written by Jeff Kaleshi

from ldap3 import Connection, SUBTREE, core

from app.users.models import User
from .util import get_permissions, get_paid_status, generate_user_data

class Groups():

    def __init__(self, config):
        self._config = config

    def get_group_members(self, group_name):
        '''
            Retrieves the users of a group from ldap
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

        connection.search(
            search_base='ou=ACMUsers,dc=acm,dc=cs',
            search_filter='(memberOf=CN={},OU=ACMGroups,DC=acm,DC=cs)'.format(group_name),
            search_scope=SUBTREE,
            attributes=['displayName', 'name', 'mail', 'memberOf', 'sAMAccountName', 'uidNumber']
            )

        users = []
        if connection.entries:
            for query in connection.entries:
                user_data = generate_user_data(query)
                user = User(**user_data)
                users.append(user)

        connection.unbind()
        return users