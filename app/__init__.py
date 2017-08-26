# app/__init__.py
# Written by Jeff Kaleshi

from flask import Flask

from config import config
from .ldap import LDAP

ldap = LDAP()

def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(config[environment])

    # Initialize apps
    ldap.init_app(app)

    # Register Routes
    from app.users.controllers import users
    app.register_blueprint(users)

    from app.groups.controllers import groups
    app.register_blueprint(groups, url_prefix='/groups')

    return app