# encoding=UTF-8

# This file serves the project in production
# See http://wsgi.readthedocs.org/en/latest/

from __future__ import unicode_literals
from moya.wsgi import Application

application = Application(
    './',  # project directory
    ['local.ini', 'production.ini'],  # project settings files to load
    server='main',  # <server> tag to load
    logging='prodlogging.ini'  # logging settings
)
