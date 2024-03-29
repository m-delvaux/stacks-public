import os

from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP, AUTH_OAUTH

basedir = os.path.abspath(os.path.dirname(__file__))

superset_oauth_key = os.getenv('GOOGLE_OAUTH_KEY')
superset_oauth_secret = os.getenv('GOOGLE_OAUTH_SECRET')

print(os.environ)

ROW_LIMIT = 5000
SUPERSET_WORKERS = 4

SECRET_KEY = 'RPY9U2Eu63D2IRnekEaq3lSQbRHvqDIFq9GXwj3d19no76LN9ukoPa2hTjBN4YJyralnrkwIzrkrz8rD16oIuPRxBjmzzdvvWh3a'

CSRF_ENABLED = False

SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
WTF_CSRF_ENABLED = False
TALISMAN_ENABLED = False

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
        'api_base_url': 'https://www.googleapis.com/oauth2/v2/',
        'client_kwargs': {
            'scope': 'openid email profile'
        },
        'request_token_url': None,
        'access_token_url': 'https://accounts.google.com/o/oauth2/token',
        'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
        'jwks_uri': 'https://www.googleapis.com/oauth2/v3/certs',
        'client_id': superset_oauth_key,
        'client_secret': superset_oauth_secret
    }
}
]

