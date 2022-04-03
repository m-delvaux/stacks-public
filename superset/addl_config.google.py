import os
from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP, AUTH_OAUTH

basedir = os.path.abspath(os.path.dirname(__file__))

ROW_LIMIT = 5000
SUPERSET_WORKERS = 4

SECRET_KEY = '9y76jZCc1eu7g11wQyWxeva5OWRB4j1e5m0zJDcpotKc01spVO54A6C83jcu'

CSRF_ENABLED = True

AUTH_TYPE = AUTH_OAUTH

AUTH_USER_REGISTRATION = True

# NOTICE:
AUTH_USER_REGISTRATION_ROLE = 'Admin'

OAUTH_PROVIDERS = [
    {
        'name': 'google',
        'icon': 'fa-google',
        'token_key': 'access_token',
        'remote_app': {
            'base_url': 'https://www.googleapis.com/oauth2/v2/',
            'request_token_params': {
                'scope': 'https://www.googleapis.com/auth/userinfo.email'
            },
            'request_token_url': None,
            'access_token_url': 'https://accounts.google.com/o/oauth2/token',
            'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
            'consumer_key': '__CLIENT_ID__',
            'consumer_secret': '__CLIENT_SECRET__'
        }
    }
]