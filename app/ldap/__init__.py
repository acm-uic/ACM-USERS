# ldap/__init__.py
# Written by Jeff Kaleshi

from .config import LDAPConfig
from .users import Users
from .groups import Groups

class LDAP():
    '''
        Manages transactions to ldap servers
    '''
    def init_app(self, app):
        self._config = LDAPConfig(app)
        self.users = Users(self._config)
        self.groups = Groups(self._config)