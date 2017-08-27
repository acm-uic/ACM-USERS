# wsgi.py
# Written by Jeff Kaleshi

import os

from app import create_app

app = create_app(os.environ['ENVIRONMENT'])
