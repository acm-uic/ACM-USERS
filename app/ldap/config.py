from ldap3 import ServerPool, Server, ROUND_ROBIN

class LDAPConfig():

    def __init__(self, app):
        ldap_servers = app.config['LDAP_SERVERS']
        ldap_port = app.config['LDAP_PORT']
        use_ssl = app.config['USE_SSL']

        ldap_pool = []
        for server in ldap_servers:
            ldap_pool.append(
                Server(server, ldap_port, use_ssl)
            )

        self.username = app.config['LDAP_SERVICE_USER']
        self.password = app.config['LDAP_SERVICE_PASS']
        self.server_pool = ServerPool(ldap_pool, ROUND_ROBIN, active=False)