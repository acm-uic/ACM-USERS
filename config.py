# config.py
# Written by Jeff Kaleshi

import os

class Config:
    SECRET_KEY = os.environ['SECRET_KEY']

    # LDAP SETTINGS
    LDAP_SERVERS = ['ad1', 'ad2', 'ad3']
    LDAP_PORT = 636
    LDAP_SERVICE_USER = os.environ['LDAP_SERVICE_USER']
    LDAP_SERVICE_PASS = os.environ['LDAP_SERVICE_PASS']
    USE_SSL = True

class DevelopConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    pass

class ProductionConfig(Config):
    pass


config = {
    'development': DevelopConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}